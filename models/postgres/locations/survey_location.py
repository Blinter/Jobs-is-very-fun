"""
DB Models
Postgres
Survey Locations Table
"""

from extensions_sql import db


class SurveyLocation(db.Model):
    """
    Many-To-Many relationship that shows the described Locations of a
    user-provided survey.
    """
    __bind_key__ = "postgres"

    __tablename__ = "survey_locations"

    survey_id = db.Column(
        db.BigInteger,
        db.ForeignKey('surveys.id'),
        primary_key=True
    )

    survey = db.relationship(
        'Survey',
        back_populates='survey_locations',
        lazy='select',
        viewonly=True
    )

    location_id = db.Column(
        db.Integer,
        db.ForeignKey('locations.id'),
        primary_key=True
    )

    location = db.relationship(
        'Location',
        back_populates='survey_locations',
        lazy='select',
        viewonly=True
    )

    def __repr__(self):
        """Show info about Survey Location."""

        return ("<SurveyLocation "
                
                f"survey={str(self.survey)} "
                
                f"location={str(self.location)} "
                
                ">")
