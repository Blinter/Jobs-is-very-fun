"""
DB Models
Postgres
Listed Job Experience Levels Table
"""

from extensions_sql import db


class ListedJobExperienceLevel(db.Model):
    """
    Many-To-Many relationship that shows the described experience levels of a
    user-provided survey.
    """
    __bind_key__ = "postgres"

    __tablename__ = "listed_job_experience_levels"

    listed_job_id = db.Column(
        db.BigInteger,
        db.ForeignKey('listed_jobs.id'),
        primary_key=True
    )

    listed_job = db.relationship(
        'ListedJob',
        back_populates="listed_job_experience_levels",
        lazy='select',
        viewonly=True
    )

    experience_level_id = db.Column(
        db.Integer,
        db.ForeignKey('experience_levels.id'),
        primary_key=True
    )

    experience_level = db.relationship(
        'ExperienceLevel',
        back_populates="listed_job_experience_levels",
        lazy='select',
        viewonly=True
    )

    def __repr__(self):
        """Show info about Listed Job Experience Levels."""

        return ("<ListedJobExperienceLevel "
                
                f"listed_job={str(self.listed_job)} "
                
                f"experience_level={str(self.experience_level)} "
                
                ">")

    @db.orm.declared_attr
    def __table_args__(self):
        return (
            db.Index(
                'idx_listed_job_experience_level_listed_job_id',
                self.listed_job_id,
                postgresql_using='hash'
            ),
            db.Index(
                'idx_listed_job_experience_level_experience_level_id',
                self.experience_level_id,
                postgresql_using='hash'
            ),
        )
