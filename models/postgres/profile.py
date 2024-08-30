"""
DB Models
Postgres
Profile Table
"""

from extensions_sql import db
from models.mariadb.resume_text import ResumeText


class Profile(db.Model):
    """
    Profile Object which holds the relationships that hold data such as
    surveys and resumes to be used for processing on the website.
    """
    __bind_key__ = "postgres"

    __tablename__ = "profiles"

    id = db.Column(
        db.BigInteger,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.VARCHAR(length=32),
        nullable=True
    )

    user_id = db.Column(
        db.BigInteger,
        db.ForeignKey('users.id'),
        nullable=False
    )

    active = db.Column(
        db.Boolean,
        nullable=False,
        default=False,
    )

    user = db.relationship(
        'User',
        back_populates="profiles",
        lazy='select',
        viewonly=True
    )

    surveys = db.relationship(
        'Survey',
        back_populates="profile",
        cascade="all, delete",
        lazy='select'
    )

    resumes = db.relationship(
        'Resume',
        back_populates="profile",
        cascade="all, delete",
        lazy='select'
    )

    saved_jobs = db.relationship(
        'SavedJob',
        back_populates="user_profile",
        cascade="all, delete",
        lazy='select'
    )

    saved_companies = db.relationship(
        'SavedCompany',
        back_populates="user_profile",
        cascade="all, delete",
        lazy='select'
    )

    def __repr__(self):
        """
        Show info about Profile.
        """

        return ("<Profile "
                f"id={str(self.id)} "
                
                f"name={str(self.name)} " +

                f"user={str(self.user)} " +
                f"active={str(self.active)} " +

                ((("[trunc.] " if len(str(self.surveys)) > 32 else "") +
                  f"surveys={str(self.surveys)[:32]} "
                  if len(str(self.surveys)) > 0 else "")
                 if self.surveys is not None else '') +

                ((("[trunc.] " if len(str(self.resumes)) > 32 else "") +
                  f"resumes={str(self.resumes)[:32]} "
                  if len(self.resumes) > 0 else "")
                 if self.resumes is not None else '') +

                ">")

    def delete(self, session: db.session):
        """
        Delete all associated MariaDB text ID's stored in resume list.
        """
        for resume in self.created_resumes:
            if resume.mariadb_text_id is not None:
                session.execute(
                    ResumeText.__table__.delete().where(
                        ResumeText.id == int(resume.mariadb_text_id))
                )
        session.delete(self)

    def to_dict_rest(self):
        """
        Convert a profile into a dictionary which can be received by a client
        as an object using REST.
        """
        return {
            'id': self.id,
            'name': self.name,
            'active': self.active
        }

    def to_dict_jinja(self):
        """
        Convert a profile into a dictionary which can be interpreted by a
        jinja template.
        """
        return {
            'id': self.id,
            'name': self.name,
            'active': self.active,
            'surveys': self.surveys if self.surveys else None,
            'resumes': self.resumes if self.resumes else None
        }


update_active_function_ddl = db.DDL(f"""\
CREATE OR REPLACE FUNCTION enforce_single_active_profile()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.active THEN
        -- Set all other profiles for the same user_id to inactive
        UPDATE profiles
        SET active = FALSE
        WHERE user_id = NEW.user_id
        AND id != NEW.id;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;\
""")

update_active_trigger_ddl = db.DDL(f"""\
CREATE TRIGGER trigger_single_active_profile
BEFORE INSERT OR UPDATE ON profiles
FOR EACH ROW
EXECUTE FUNCTION enforce_single_active_profile();\
""")

db.event.listen(Profile.__table__, 'after_create', update_active_function_ddl)
db.event.listen(Profile.__table__, 'after_create', update_active_trigger_ddl)
