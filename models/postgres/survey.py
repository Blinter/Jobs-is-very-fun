"""
DB Models
Postgres
Survey Table
"""

from extensions_sql import db


class Survey(db.Model):
    """
    Holds data to be used for database routines and job matches which are fed
    to the user.
    """
    __bind_key__ = "postgres"

    __tablename__ = "surveys"

    id = db.Column(
        db.BigInteger,
        primary_key=True,
        autoincrement=True
    )

    profile_id = db.Column(
        db.BigInteger,
        db.ForeignKey('profiles.id'),
        nullable=False,
    )

    profile = db.relationship(
        "Profile",
        back_populates="surveys",
        lazy='select',
        viewonly=True
    )

    survey_locations = db.relationship(
        'SurveyLocation',
        back_populates="survey",
        cascade="all, delete",
        lazy='select'
    )

    survey_job_types = db.relationship(
        'SurveyJobType',
        back_populates="survey",
        cascade="all, delete",
        lazy='select'
    )

    survey_experience_levels = db.relationship(
        'SurveyExperienceLevel',
        back_populates="survey",
        cascade="all, delete",
        lazy='select'
    )

    salary_currency = db.Column(
        db.VARCHAR(length=12),
        nullable=True,
        default="USD"
    )

    salary_range_min = db.Column(
        db.BigInteger,
        nullable=True
    )

    salary_range_max = db.Column(
        db.BigInteger,
        nullable=True
    )

    def __repr__(self):
        """Show info about Survey."""

        return ("<Survey "
                f"id={str(self.id)} "
                f"profile_id={str(self.profile)} " +

                ((("[trunc.] "
                   if len(str(self.survey_profiles)) > 32 else "") +
                  f"survey_profiles={str(self.survey_profiles)[:32]} "
                  if len(str(self.survey_profiles)) > 0 else "")
                 if self.survey_profiles is not None else '') +

                ((("[trunc.] "
                   if len(str(self.survey_locations)) > 32 else "") +
                  f"survey_locations={str(self.survey_locations)[:32]} "
                  if len(str(self.survey_locations)) > 0 else "")
                 if self.survey_locations is not None else '') +

                ((("[trunc.]"
                   if len(str(self.survey_job_types)) > 32 else "") +
                  f"survey_job_types={str(self.survey_job_types)[:32]} "
                  if len(str(self.survey_job_types)) > 0 else "")
                 if self.survey_job_type is not None else '') +

                ((("[trunc.]"
                   if len(str(self.survey_experience_levels)) > 32 else "") +
                  "survey_experience_levels="
                  f"{str(self.survey_experience_levels)[:32]} "
                  if len(str(self.survey_experience_levels)) > 0 else "")
                 if self.survey_experience_levels is not None else '') +

                ">")
