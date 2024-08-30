import requests
from flask import (
    Blueprint,
    redirect,
    url_for,
    session,
    request,
    flash
)

from google.auth.exceptions import GoogleAuthError, RefreshError
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import google_auth_oauthlib.flow
from sqlalchemy import exists, or_, and_
from sqlalchemy.exc import SQLAlchemyError, OperationalError, IntegrityError

from app import db
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
from secrets_jobs.credentials import sso_google_secrets_path

from extensions_profiles import user_check_set_active_profile

sso_google_bp = Blueprint(
    'sso_google',
    __name__
)

# Session variables
# session.pop('sso_google_token') Google Credentials Dictionary
# session.pop('sso_google_state') - Google Generated Hash
# session.pop('sso_google_id')  Google Generated Number
# session.pop('sso_google_email') Used in registration
# session.pop('sso_google_image') 96x96


@sso_google_bp.route(
    "/sso_google"
)
def sso_google():
    """
    This route is used to authorize a new user by using Google.
    Google provides a state session object for use to mitigate CSRF.
    """

    # Check if user is already logged in.
    if session.get('user_id', False):
        flash(
            "Sorry, you cannot access this page since you are already "
            "logged in.",
            'danger'
        )
        return redirect(url_for('general.home'))

    # Check if GitHub token is found
    if session.get('sso_github_token', False):
        flash(
            "Sorry, you cannot access this page since you are logged in "
            "through GitHub.",
            'danger'
        )

        # Send the user back to the homepage.
        return redirect(url_for('general.home'))

    # Check if user already has a Google Token
    if session.get('sso_google_token', False):
        flash(
            "You have already been logged in using Google",
            'danger'
        )

        return redirect(url_for('general.home'))

    # Access email and profile ID data (Scopes)
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        sso_google_secrets_path,
        scopes=['openid', 'https://www.googleapis.com/auth/userinfo.email'],
        redirect_uri=(
            url_for(
                'sso_google.sso_google_callback',
                _external=True
            )
        )
    )

    # Create state and authorization URL for User
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true',
        prompt='consent'
    )

    # Set Google State
    session['sso_google_state'] = state

    # Redirect User to authorization URL
    return redirect(authorization_url)


@sso_google_bp.route(
    "/sso_google_callback"
)
def sso_google_callback():
    """
    This route is the callback URL that the Google App is allowed to redirect
    to.

    Finalize checks before inserting a new user into the database.
    """
    if session.get('user_id', False):
        flash(
            "Sorry, you cannot access this page since you are already "
            "logged in.",
            'danger'
        )
        return redirect(url_for('general.home'))

    # Check if GitHub token is found
    if session.get('sso_github_token', False):
        flash(
            "Sorry, you cannot access this page since you are logged in "
            "through GitHub.",
            'danger'
        )

        # Send the user back to the homepage.
        return redirect(url_for('general.home'))

    state = session.get('sso_google_state', False)
    if not state:
        if session.get('sso_google_token', False):
            session.pop('sso_google_token', None)

        # send back to home page
        return redirect(url_for('general.home'))

    # Access email and profile ID data (Scopes)
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        sso_google_secrets_path,
        scopes=['openid', 'https://www.googleapis.com/auth/userinfo.email'],
        state=state,
        redirect_uri=(
            url_for(
                'sso_google.sso_google_callback',
                _external=True
            )
        )
    )

    # Fetch token with auth response
    flow.fetch_token(authorization_response=request.url)

    # Set credentials as flow.credentials
    credentials = flow.credentials

    # Set session object
    session['sso_google_token'] = sso_google_credentials_to_dict(credentials)

    try:
        # Grab user info using credentials object
        user_info = sso_google_get_user_info(credentials)

        # Set variables here from Google Profile for convenience
        temp_google_id = str(user_info['id'])
        temp_google_email = str(user_info['email'])
        temp_google_verified_email = str(user_info['verified_email'])
        temp_google_image = str(user_info['picture'])

        # Check if Google Email is set
        if len(temp_google_email) == 0:
            sso_google_logout()

            flash(
                "Sorry, there was an error reading your Google details. Try "
                "again.",
                'danger'
            )

            # Redirect user to home
            return redirect(url_for('general.home'))

        # Check if Google ID is set
        if len(temp_google_id) == 0:
            # Log out user

            # Clear Session
            if session.get('sso_google_token', False):
                session.pop('sso_google_token', None)

            clear_google_session()

            flash(
                "Sorry, there was an error reading your Google details. Try "
                "again.",
                'danger'
            )

            # Redirect user to home
            return redirect(url_for('general.home'))

        # Avatar link check - since Google manages this endpoint
        # avatar image URL issues should only arise if google updates the way
        # that their users can store their images.
        if 'googleusercontent.com' not in temp_google_image:
            # pass anyway but with no image link.
            temp_google_image = ""

        # check that there is a verified_email.
        if not temp_google_verified_email:
            # This account cannot be used for login since email is not verified.
            # Logout user

            # Clear Session
            if session.get('sso_google_token', False):
                session.pop('sso_google_token', None)

            clear_google_session()

            flash(
                "Sorry, you cannot register since you have no emails associated"
                " with your Google account that have been verified.",
                'danger'
            )

            return redirect(url_for('general.home'))

        registration_email = temp_google_email

        # if ID already exists: then log them in.
        # if other details such as email are already associated with a user,
        # prevent the user from registering and delete their access
        # token. The site requires a unique email address.

        # Check if Google ID is already in database
        # if so, refresh their details and log them in.

        if (db.session.query(exists().where(
                User.google_sso_id == temp_google_id)).scalar()):
            existing_user = db.session.query(User).filter(
                User.google_sso_id == temp_google_id).first()

            # Check to make sure a new email address is not registered to
            # another account.
            if (existing_user.google_sso_email != registration_email and
                    db.session.query(exists().where(
                        and_(
                            temp_google_id != User.google_sso_id,
                            or_(
                                registration_email == User.github_sso_email,
                                registration_email == User.google_sso_email,
                                registration_email == User.email
                            )
                        )
                    ))):

                # Remove Google Authorization for this token.
                if session.get('sso_google_token', False):
                    if google_logout(credentials):
                        # Clear Session
                        if session.get('sso_google_token', False):
                            session.pop('sso_google_token', None)

                        clear_google_session()

                    flash(
                        "Google authorization revoked.",
                        'success'
                    )

                else:

                    flash(
                        "Google didn't allow us to revoke your user token.",
                        'danger'
                    )

                    # Clear Session Anyway
                    if session.get('sso_google_token', False):
                        session.pop('sso_google_token', None)

                    clear_google_session()
                    db.session.close()

                    return redirect(url_for('user.logout'))

                flash(
                    "The primary email associated with your Google account is "
                    "already registered to a separate account. Set a different "
                    "primary email address for your Google account then try "
                    "again.",
                    'danger'
                )

                db.session.close()

                # Redirect user to homepage
                return redirect(url_for('general.home'))

            # Add session tokens
            session['user_id'] = existing_user.id

            session['sso_google'] = True
            session['sso_google_id'] = existing_user.google_sso_id

            temp_changed_email = False
            temp_changed_image = False

            if existing_user.google_sso_email != registration_email:
                # Update the existing email to reflect new changes.
                existing_user.google_sso_email = registration_email
                temp_changed_email = True

            if (len(str(existing_user.google_sso_image)) != 0 and
                    existing_user.google_sso_image != temp_google_image):
                # Update the existing email to reflect new changes.
                existing_user.google_sso_image = temp_google_image

                temp_changed_image = True

            if existing_user.google_sso_image:
                session['google_sso_image'] = existing_user.google_sso_image

            session['sso_google_email'] = existing_user.google_sso_email

            # Finally, commit to database if there were changes.
            if (temp_changed_email or
                    temp_changed_image):
                db.session.commit()

            flash(
                "You have been logged in as " +
                str(existing_user.google_sso_email),
                'success'
            )

            user_check_set_active_profile()

            db.session.close()

            return redirect(url_for('general.home'))
        # do database function here
        new_user = User(
            google_sso=True,
            google_sso_id=temp_google_id,
            google_sso_email=temp_google_email,
            google_sso_image=temp_google_image
        )

        db.session.add(new_user)
        # Finally, commit to database and set session objects.
        db.session.commit()

        session['user_id'] = new_user.id

        session['sso_google'] = True
        session['sso_google_id'] = new_user.google_sso_id
        session['sso_google_email'] = new_user.google_sso_email
        session['sso_google_image'] = new_user.google_sso_image

        flash(
            "Your Google account has been registered with our website.",
            'success'
        )

        db.session.close()

        return redirect(url_for('general.home'))

    # Catch Google Authentication Error
    except GoogleAuthError:
        db.session.rollback()
        db.session.close()
        # Clear Google Session
        if session.get('sso_google_token', False):
            session.pop('sso_google_token', None)

        clear_google_session()

        # Attempt to retry Authentication.
        return redirect(
            url_for(
                'sso_google.sso_google_callback',
                _external=True
            )
        )

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.rollback()
        db.session.close()
        # Clear Google Session
        if session.get('sso_google_token', False):
            session.pop('sso_google_token', None)

        clear_google_session()

        print(f"IntegrityError: {e}")
        flash(
            "There was an error. Try again later.",
            'danger'
        )
        # Redirect the user back to homepage.
        return redirect(url_for('general.home'))

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.rollback()
        db.session.close()
        # Clear Google Session
        if session.get('sso_google_token', False):
            session.pop('sso_google_token', None)

        clear_google_session()

        print(f"OperationalError: {e}")
        flash(
            "There was an error. Try again later.",
            'danger'
        )
        # Redirect the user back to homepage.
        return redirect(url_for('general.home'))

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.rollback()
        db.session.close()
        # Clear Google Session
        if session.get('sso_google_token', False):
            session.pop('sso_google_token', None)

        clear_google_session()

        print(f"SQLAlchemyError: {e}")
        flash(
            "There was an error. Try again later.",
            'danger'
        )
        # Redirect the user back to homepage.
        return redirect(url_for('general.home'))

    # Other Errors
    except Exception as e:
        db.session.rollback()
        db.session.close()

        # Clear Google Session
        if session.get('sso_google_token', False):
            session.pop('sso_google_token', None)

        clear_google_session()

        print(f"Error: {e}")
        flash(
            "There was an error. Try again later.",
            'danger'
        )
        # Redirect the user back to homepage.
        return redirect(url_for('general.home'))


@sso_google_bp.route(
    "/sso_google_logout"
)
def sso_google_logout():
    """
    This route is used to remove a user from Google authorization.

    The User Table no longer has any associated details with it and
    all user data will be completely deleted.
    """

    # Check if user is not logged in.
    if not session.get('user_id', False):
        flash(
            "Sorry, you cannot access this page since you are not logged in.",
            'danger'
        )

        # Send the user back to the homepage.
        return redirect(url_for('general.home'))

    # Check if GitHub token is found
    if session.get('sso_github_token', False):
        flash(
            "Sorry, you cannot access this page since you are logged in "
            "through GitHub.",
            'danger'
        )

        # Send the user back to the homepage.
        return redirect(url_for('general.home'))

    # Check if Google token is not set.
    if not session.get('sso_google_token', False):
        flash(
            "Google token not available",
            'danger'
        )

        # Send the user back to the homepage.
        return redirect(url_for('general.home'))

    # Retrieve the credentials dictionary
    credentials = sso_google_credentials_from_dict(
        session.get('sso_google_token', False))

    # Check if credentials are valid and attempt to refresh the Google Token.
    if (not credentials or
            not credentials.valid):

        # Check if credentials expired
        if (credentials and
                credentials.expired and
                credentials.refresh_token):
            try:

                # Refresh the Google Token
                credentials.refresh(Request())

            # Catch Refresh Error
            except RefreshError:

                # Clear Google Session
                if session.get('sso_google_token', False):
                    session.pop('sso_google_token', None)

                clear_google_session()

                # Log the user out to clear session objects.
                return redirect(url_for('user.logout'))

            # Continue and set sso_google_token session object.
            session['sso_google_token'] = (
                sso_google_credentials_to_dict(credentials)
            )

        else:

            # Clear Google Session
            if session.get('sso_google_token', False):
                session.pop('sso_google_token', None)

            clear_google_session()

            # Log the user out to clear session objects.
            return redirect(url_for('user.logout'))

    try:
        # Revoke support for log out is limited
        # use refresh_token instead of token, allowing successful logout.
        revoke = requests.post(
            url="https://oauth2.googleapis.com/revoke",
            data={'token': credentials.refresh_token},
            headers={"Content-Type": "application/x-www-form-urlencoded"})

        # Debugging messages
        # revoke.raise_for_status()

        # Store response from Google in status_code
        status_code = getattr(revoke, 'status_code')

        # Check if revoke was successful.
        if status_code == 200:

            temp_id = session.get('user_id', False)
            if temp_id:
                if (db.session.query(exists().where(
                        User.id == int(temp_id))).scalar()):
                    # Select the User
                    existing_user = db.session.query(User).filter(
                        User.id == int(temp_id)).first()

                    # Delete the User
                    db.session.delete(existing_user)

                    # Commit to Database
                    db.session.commit()

            # Clear Session
            if session.get('sso_google_token', False):
                session.pop('sso_google_token', None)

            clear_google_session()

            # Send the user back to the homepage.
            flash(
                "Successfully logged out of Google SSO.",
                'success'
            )

            db.session.close()

            return redirect(url_for('general.home'))

        else:
            flash(
                str(credentials.refresh_token) +
                " An error occurred. Status Code: " + str(status_code),
                'danger'
            )

            db.session.close()

            # Send the user back to the homepage.
            return redirect(url_for('general.home'))

    # Catch Google Authentication Error
    except GoogleAuthError:
        db.session.rollback()
        db.session.close()

        # Clear Google Session
        if session.get('sso_google_token', False):
            session.pop('sso_google_token', None)

        clear_google_session()

        # Attempt to retry Authentication.
        return redirect(
            url_for(
                'sso_google.sso_google_callback',
                _external=True
            )
        )


def google_logout(credentials):
    """
    Access Google API and remove app authorization.
    """
    try:
        # Revoke support for log out is limited
        # use refresh_token instead of token, allowing successful logout.
        revoke = requests.post(
            url="https://oauth2.googleapis.com/revoke",
            data={'token': credentials.refresh_token},
            headers={"Content-Type": "application/x-www-form-urlencoded"})

        # Return Boolean if Status Code was successful.
        return 200 == getattr(revoke, 'status_code')

    # Catch Google Authentication Error
    except GoogleAuthError:

        # Clear Google Session
        if session.get('sso_google_token', False):
            session.pop('sso_google_token', None)

        clear_google_session()

        return False


def sso_google_get_user_info(credentials):
    """
    Access Google API and retrieve required account details
    """
    userinfo_service = build('oauth2', 'v2', credentials=credentials)
    user_info = userinfo_service.userinfo().get().execute()
    return user_info


def sso_google_credentials_to_dict(credentials):
    """
    Google provided sample to convert their token data to a dictionary.
    """
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }


def sso_google_credentials_from_dict(credentials_dict):
    """
    Google provided sample to organize their token data into a Credentials
    object.
    """
    return Credentials(
        token=credentials_dict['token'],
        refresh_token=credentials_dict.get('refresh_token'),
        token_uri=credentials_dict['token_uri'],
        client_id=credentials_dict['client_id'],
        client_secret=credentials_dict['client_secret'],
        scopes=credentials_dict['scopes']
    )


def clear_google_session():
    """
    Clear Google Session from server
    This does not include GitHub App Authorization
    """
    if session.get('user_id', False):
        session.pop('user_id', None)

    if session.get('profile_id', False):
        session.pop('profile_id', None)

    if session.get('sso_google_token', False):
        session.pop('sso_google_token', None)

    if session.get('sso_google', False):
        session.pop('sso_google', None)

    if session.get('sso_google_id', False):
        session.pop('sso_google_id', None)

    if session.get('sso_google_name', False):
        session.pop('sso_google_name', None)

    if session.get('sso_google_email', False):
        session.pop('sso_google_email', None)

    if session.get('sso_google_image', False):
        session.pop('sso_google_image', None)


# Development only
@sso_google_bp.route(
    "/sso_google_info"
)
def sso_google_info():
    """
    This function is here for debugging purposes, if Google changes the way that
    they do authorization.
    This shows sensitive data provided by SSO logins so disable during
    production.
    """

    # Check if user is not logged in.
    if not session.get('user_id', False):
        flash(
            "Sorry, you cannot access this page since you are not logged in.",
            'danger'
        )

        # Send the user back to the homepage.
        return redirect(url_for('general.home'))

    # Check if GitHub token is found
    if session.get('sso_github_token', False):
        flash(
            "Sorry, you cannot access this page since you are logged in "
            "through GitHub.",
            'danger'
        )

        # Send the user back to the homepage.
        return redirect(url_for('general.home'))

    # Check if Google token is not set.
    if not session.get('sso_google_token', False):
        flash(
            "Google token not available",
            'danger'
        )

        # Send the user back to the homepage.
        return redirect(url_for('general.home'))

    # Retrieve the credentials dictionary
    credentials = sso_google_credentials_from_dict(
        session.get('sso_google_token', False))

    # Check if credentials are valid and attempt to refresh the Google Token.
    if (not credentials or
            not credentials.valid):

        # Check if credentials expired
        if (credentials and
                credentials.expired and
                credentials.refresh_token):
            try:

                # Refresh the Google Token
                credentials.refresh(Request())

            # Catch Refresh Error
            except RefreshError:

                # Clear Google Session
                if session.get('sso_google_token', False):
                    session.pop('sso_google_token', None)

                clear_google_session()

                # Log the user out to clear session objects.
                return redirect(url_for('user.logout'))

            # Continue and set sso_google_token session object.
            session['sso_google_token'] = (
                sso_google_credentials_to_dict(credentials))

        else:

            # Clear Google Session
            if session.get('sso_google_token', False):
                session.pop('sso_google_token', None)

            clear_google_session()

            # Log the user out to clear session objects.
            return redirect(url_for('user.logout'))

    try:

        # Retrieve the Google User info and return it to the user.
        user_info = (
            build('oauth2', 'v2', credentials=credentials)
            .userinfo()
            .get()
            .execute()
        )

        return_string = "Login: " + str(user_info['email']) + "<br/>"

        return_string += ("Verified Email: " +
                          str(user_info['verified_email']) + "<br/>")

        return_string += "ID: " + str(user_info['id']) + "<br/>"

        return_string += ("Avatar URL: " + str(user_info['picture']) +
                          "<br/>")

        return_string += ("Avatar: <br/> <img src=" +
                          str(user_info['picture'])) + " /><br/><hr/>"

        return return_string

    # Catch Google Authentication Error
    except GoogleAuthError:
        # Clear Google Session
        if session.get('sso_google_token', False):
            session.pop('sso_google_token', None)

        clear_google_session()

        # Redirect the user to Logout
        return redirect(url_for('user.logout'))


# Development only
@sso_google_bp.route(
    "/sso_google_check"
)
def sso_google_check():
    """
    This function is here for debugging purposes, if Google changes the way that
    they do authorization.
    This shows sensitive data provided by SSO logins so disable during
    production.
    """

    # Check if user is not logged in.
    if not session.get('user_id', False):
        flash(
            "Sorry, you cannot access this page since you are not logged in.",
            'danger'
        )

        # Send the user back to the homepage.
        return redirect(url_for('general.home'))

    # Check if GitHub token is found
    if session.get('sso_github_token', False):
        flash(
            "Sorry, you cannot access this page since you are logged in "
            "through GitHub.",
            'danger'
        )

        # Send the user back to the homepage.
        return redirect(url_for('general.home'))

    # Check if Google token is not set.
    if not session.get('sso_google_token', False):
        flash(
            "Google token not available",
            'danger'
        )

        # Send the user back to the homepage.
        return redirect(url_for('general.home'))

    # Retrieve the credentials dictionary
    credentials = sso_google_credentials_from_dict(
        session.get('sso_google_token', False))

    # Check if credentials are valid and attempt to refresh the Google Token.
    if (not credentials or
            not credentials.valid):

        # Check if credentials expired
        if (credentials and
                credentials.expired and
                credentials.refresh_token):
            try:

                # Refresh the Google Token
                credentials.refresh(Request())

            # Catch Refresh Error
            except RefreshError:

                # Clear Google Session
                if session.get('sso_google_token', False):
                    session.pop('sso_google_token', None)

                clear_google_session()

                # Log the user out to clear session objects.
                return redirect(url_for('user.logout'))

            # Continue and set sso_google_token session object.
            session['sso_google_token'] = (
                sso_google_credentials_to_dict(credentials))

        else:

            # Clear Google Session
            if session.get('sso_google_token', False):
                session.pop('sso_google_token', None)

            clear_google_session()

            # Log the user out to clear session objects.
            return redirect(url_for('user.logout'))

    try:

        # Retrieve the Google User info and return it to the user.
        user_info = (
            build('oauth2', 'v2', credentials=credentials)
            .userinfo()
            .get()
            .execute()
        )

        # Return all associated user info from accessing Google's API.
        return f'User info: {user_info}'

    # Catch Google Authentication Error
    except GoogleAuthError:
        # Clear Google Session
        if session.get('sso_google_token', False):
            session.pop('sso_google_token', None)

        clear_google_session()

        # Attempt to retry Authentication.
        return redirect(
            url_for(
                'sso_google.sso_google_callback',
                _external=True
            )
        )
