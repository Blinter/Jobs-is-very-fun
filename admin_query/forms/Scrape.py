from flask_wtf import FlaskForm
from wtforms import validators, SubmitField
from wtforms.fields.simple import StringField


class Scrape(FlaskForm):
    """
    Form for submitting a manual cache request to query an API and save
    in Mongo FS then add to Mongo Scraped Storage table.

    Automatic proxy selection
    """
    URL = StringField("URL",
                      validators=[validators.input_required()]
                      )

    SubmitButton = SubmitField("Scrape")
