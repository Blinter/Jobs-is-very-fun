"""
DB Models
Postgres
Survey Job Types Table
"""

from extensions_sql import db


class SurveyJobType(db.Model):
    """
    Many-To-Many relationship that shows the described Job Types of a
    user-provided survey.
    """
    __bind_key__ = "postgres"

    __tablename__ = "survey_job_types"

    survey_id = db.Column(
        db.BigInteger,
        db.ForeignKey('surveys.id'),
        primary_key=True
    )

    survey = db.relationship(
        'Survey',
        back_populates='survey_job_types',
        lazy='select',
        viewonly=True
    )

    job_type_id = db.Column(
        db.Integer,
        db.ForeignKey('job_types.id'),
        primary_key=True
    )

    job_type = db.relationship(
        'JobType',
        back_populates='survey_job_types',
        lazy='select',
        viewonly=True
    )

    def __repr__(self):
        """Show info about Survey Job Type."""

        return ("<SurveyJobType "
                
                f"survey_={str(self.survey)} "
                
                f"job_type={str(self.job_type)} "
                
                ">")
