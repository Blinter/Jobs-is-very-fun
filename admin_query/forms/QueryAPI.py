from flask_wtf import FlaskForm
from wtforms import validators, SelectField, SubmitField, BooleanField


class QueryAPI(FlaskForm):
    """
    Form for submitting a manual cache request to query an API and save
    in Mongo FS then add to Mongo Storage table.

    Automatic proxy selection option

    Proxy ID Query to use
    API Key
    """
    API = SelectField("API", [
        validators.InputRequired(message='API cannot be empty'),
        ])

    # Since Endpoints are loaded by the admin through client-side REST,
    # skip on form validation for these fields.
    Endpoint = SelectField("Endpoint", choices=[], validate_choice=False)

    Proxy = SelectField("Proxy", [
        # validators.InputRequired(message='Proxy cannot be empty'),
        validators.optional(),
        ])

    # Since API Keys are loaded by the admin through client-side REST, skip on
    # form validation for these fields.
    APIKey = SelectField("API Key", choices=[], validate_choice=False)

    APIKeyAuto = BooleanField("Automatic API Key", [
        # validators.InputRequired(message='Proxy cannot be empty'),
        validators.optional(),
        ])

    SubmitButton = SubmitField("Query")
