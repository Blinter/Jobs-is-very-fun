"""
DB Models
Postgres
Experience Levels Table
"""

from extensions_sql import db


class ExperienceLevel(db.Model):
    """
    Referred to by Listed Job or Survey
    """
    __bind_key__ = "postgres"

    __tablename__ = "experience_levels"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.VARCHAR,
        nullable=False,
    )

    survey_experience_levels = db.relationship(
        'SurveyExperienceLevel',
        back_populates="experience_level",
        cascade="all, delete",
        lazy='select'
    )

    listed_job_experience_levels = db.relationship(
        'ListedJobExperienceLevel',
        back_populates="experience_level",
        cascade="all, delete",
        lazy='select'
    )

    def __repr__(self):
        """Show info about Job Type."""

        return ("<ExperienceLevel "
                
                f"id={str(self.id)} "
                
                f"name={str(self.name)} " +

                ((("[trunc.] "
                   if len(str(self.survey_experience_levels)) > 64 else "") +
                  "survey_job_types="
                  f"{str(str(self.survey_experience_levels))[:64]} "
                  if len(str(self.survey_experience_levels)) > 0 else '')
                 if self.survey_experience_levels is not None else '') +

                ((("[trunc.] "
                   if len(str(self.listed_job_experience_levels)) > 64
                   else "") +
                  "listed_job_experience_levels="
                  f"{str(self.listed_job_experience_levels)[:64]} "
                  if len(str(self.listed_job_experience_levels)) > 0 else '')
                 if self.listed_job_experience_levels is not None else '') +

                ">")
