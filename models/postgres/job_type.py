"""
DB Models
Postgres
Job Type Table
"""

from extensions_sql import db


class JobType(db.Model):
    """
    Referred to by Listed Job or Survey
    """
    __bind_key__ = "postgres"

    __tablename__ = "job_types"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.VARCHAR,
        nullable=False,
        unique=True
    )

    survey_job_types = db.relationship(
        'SurveyJobType',
        back_populates="job_type",
        cascade="all, delete",
        lazy='select'
    )

    listed_job_job_types = db.relationship(
        'ListedJobJobType',
        back_populates="job_type",
        cascade="all, delete",
        lazy='select'
    )

    def __repr__(self):
        """Show info about Job Type."""

        return ("<JobType "
                f"id={str(self.id)} "
                f"name={str(self.name)}" +

                ((("[trunc.]" if len(str(self.survey_job_types)) > 64 else "") +
                  f"survey_job_types={str(str(self.survey_job_types))[:64]} "
                  if len(str(self.survey_job_types)) > 0 else '')
                 if self.survey_job_types is not None else '') +

                ((("[trunc.]" if len(str(self.listed_job_job_types)) > 64
                   else "") +
                  f"listed_job_job_types={str(self.listed_job_job_types)[:64]} "
                  if len(str(self.listed_job_job_types)) > 0 else '')
                 if self.listed_job_job_types is not None else '') +

                ">")
