import requests
from flask import session, url_for
from sqlalchemy import exists

from extensions_sql import db

# Imports are required due to relationships
from models.postgres.locations.x_location_id import XLocationID
from models.postgres.locations.glassdoor_location_id import GlassdoorLocationID
from models.postgres.locations.linkedin_geourn_id import LinkedInGeoURNID

from models.postgres.api_source import APISource
from models.postgres.company import Company
from models.postgres.locations.location import Location

from models.postgres.listed_job_experience_level import ListedJobExperienceLevel
from models.postgres.locations.listed_job_location import ListedJobLocation
from models.postgres.listed_job_job_type import ListedJobJobType

from models.postgres.job_type import JobType
from models.postgres.listed_job import ListedJob
from models.postgres.experience_level import ExperienceLevel

from models.postgres.survey_experience_level import SurveyExperienceLevel
from models.postgres.survey_job_type import SurveyJobType
from models.postgres.locations.survey_location import SurveyLocation

from models.postgres.resume import Resume
from models.postgres.survey import Survey
from models.postgres.profile import Profile

from models.postgres.saved_company import SavedCompany
from models.postgres.saved_job import SavedJob

from models.postgres.user import User

from secrets_jobs.credentials import google_recaptcha_v2_secret


def get_authenticated_user_name():
    """
    Get Username, GitHub name, or Google name to be displayed for Navigation
    bar and to distinguish login.
    """
    if not session.get('user_id', False):
        return None

    if session.get('email', False):
        return session.get('username')

    if session.get('sso_google', False):
        return session.get('sso_google_email')

    if session.get('sso_github', False):
        return session.get('sso_github_name')


def get_delete_link():
    """
    Get Username, GitHub name, or Google name to be displayed for Navigation
    bar and to distinguish login.
    """
    if not session.get('user_id', False):
        return None

    elif session.get('email', False):
        return url_for('user.user_delete')

    elif session.get('sso_google', False):
        return url_for('sso_google.sso_google_logout')

    elif session.get('sso_github', False):
        return url_for('sso_github.sso_github_logout')

    else:
        return None


def clear_email_session():
    """
    This function is used to remove session data from the user if they're
    logged in through email.
    This does not delete their data, only removes their session so that they
    can switch accounts.
    """

    if session.get('user_id', False):
        session.pop('user_id', None)

    if session.get('email', False):
        session.pop('email', None)

    if session.get('email_registration', False):
        session.pop('email_registration', None)

    if session.get('username_state', False):
        session.pop('username_state', None)

    if session.get('email_state', False):
        session.pop('email_state', None)


def get_username_from_email(email):
    """
    Get Username from Email
    Checks if email provided is valid and exists, then returns username.
    If not, None will be returned.
    """
    return (None if not email or
            email is None or
            len(str(email)) == 0 or
            len(str(email)) < 6 or
            len(str(email)) > 128 or
            str(email).find('@') == -1 or
            not db.session.query(exists().where(
                User.email == str(email))).scalar() else
            str((db.session.query(User).filter(
                User.email == str(email)).first()).username))


def get_email_from_username(username):
    """
    Get Email from Username
    Checks if username provided is valid and exists, then returns email.
    If not, None will be returned.
    """
    return (None if not username or
            username is None or
            len(str(username)) == 0 or
            len(str(username)) < 3 or
            len(str(username)) > 20 or
            str(username).find('@') != -1 or
            not db.session.query(exists().where(
                User.username == str(username))).scalar() else
            str((db.session.query(User).filter(
                User.username == str(username)).first()).email))


def google_verify_recaptcha(response_token):
    """
    Google Verify Recaptcha
    POSTs to Google API To verify that the user's captcha request is successful.
    """
    try:
        response = requests.post(
            "https://www.google.com/recaptcha/api/siteverify",
            data={
                "secret": google_recaptcha_v2_secret,
                "response": response_token
            }).json()
        return response['success']

    except Exception as e:
        # Handle Server Errors
        print(e, flush=True)
        # Allow anyway if the problem is with Google's Recaptcha servers.
        return True
