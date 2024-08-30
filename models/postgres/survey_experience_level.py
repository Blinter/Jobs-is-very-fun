"""
DB Models
Postgres
Survey Experience Levels Table
"""

from extensions_sql import db


class SurveyExperienceLevel(db.Model):
    """
    Many-To-Many relationship that shows the described experience levels of a
    user-provided survey.
    """
    __bind_key__ = "postgres"

    __tablename__ = "survey_experience_levels"

    survey_id = db.Column(
        db.BigInteger,
        db.ForeignKey('surveys.id'),
        primary_key=True
    )

    survey = db.relationship(
        'Survey',
        back_populates="survey_experience_levels",
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
        back_populates="survey_experience_levels",
        lazy='select',
        viewonly=True
    )

    def __repr__(self):
        """Show info about Survey Experience Levels."""

        return ("<SurveyExperienceLevel "
                
                f"survey={str(self.survey)} "
                
                f"experience_level={str(self.experience_level)} "
                
                ">")
