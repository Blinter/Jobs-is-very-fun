import requests
from secrets import token_urlsafe
from flask import (
    Blueprint,
    redirect,
    url_for,
    session,
    request,
    flash
)

from requests.auth import HTTPBasicAuth
from sqlalchemy import exists, and_, or_
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError

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

from secrets_jobs.credentials import (
    sso_github_id,
    sso_github_secret
)

from extensions_profiles import user_check_set_active_profile

from app import db

sso_github_bp = Blueprint(
    'sso_github',
    __name__
)


@sso_github_bp.route(
    "/sso_github"
)
def sso_github():
    """
    This route is used to authorize a new user by using GitHub.
    Create a server-side CSRF session token to protect against attacks.
    """

    # Check if user is already logged in.
    if session.get('user_id', False):
        flash(
            "Sorry, you cannot access this page since you are already "
            "logged in.",
            'danger'
        )

        # Send the user back to home page.
        return redirect(url_for('general.home'))

    # Check if user already has a GitHub Token.
    if session.get('sso_github', False):
        flash(
            "You have already been logged in using Github",
            'danger'
        )
        # Send the
        # user back to home page.
        return redirect(url_for('general.home'))

    # Pop the GitHub State
    if session.get('sso_github_state', False):
        session.pop('sso_github_state', None)

    # Create a new state token to protect against CSRF attacks. The token
    # will only be checked if it is set when the callback URL is accessed.
    session['sso_github_state'] = token_urlsafe(20)

    # Debug for ProxyFix (Reverse Proxy Configuration)
    # return str({url_for('sso_github.sso_github_callback', _external=True)})

    # Finally, redirect the user to the authorization page.
    return redirect(
        "https://github.com/login/oauth/authorize?"
        f"client_id={sso_github_id}&"
        "redirect_uri=" +
        url_for('sso_github.sso_github_callback',
                _external=True) + "&"
        f"state={session['sso_github_state']}&"
        "allow_signup=true"
    )


@sso_github_bp.route(
    "/sso_github_callback"
)
def sso_github_callback():
    """
    This route is the callback URL that the GitHub App is allowed to redirect
    to.

    Finalize checks before inserting a new user into the database.
    """

    # Check if user is already logged in.
    if session.get('user_id', False):
        flash(
            "Sorry, you cannot access this page since you are already "
            "logged in.",
            'danger'
        )

    # Check if GitHub Token has already been set
    if session.get('sso_github', False):
        flash(
            "You have already been logged in using Github",
            'danger'
        )
        # Send the
        # user back to home page.
        return redirect(url_for('general.home'))

    # Verify that GitHub authorization was accepted by the user.
    if (request and
            request.args and
            request.args.get('error', False)):
        flash(
            "Github authorization access denied.",
            'danger'
        )
        # Send the
        # user back to home page.
        return redirect(url_for('general.home'))

    sso_github_state = session.get('sso_github_state', False)

    # GitHub Authorization provides
    #
    # code (Token that was provided by GitHub after authorization)
    # state (Our token to prevent CSRF attacks)
    code = request.args.get('code', False)

    state = request.args.get('state', False)

    # Verify the state parameter to mitigate CSRF attacks
    if (not sso_github_state or
            not state or
            not code or
            str(state) != str(sso_github_state)):

        flash(
            "Sorry, there was an error. Try again.",
            'danger'
        )
        # Send the
        # user back to home page.
        return redirect(url_for('sso_github.sso_github'))

    # Pop used token that was only used for the authorization process to
    # protect against CSRF attacks.
    session.pop('sso_github_state')

    # Set the GitHub Session Token
    session['sso_github_token'] = github_access_token(code)

    # Call GitHub API and access Email and Profile data.
    email_data = github_email_data(session['sso_github_token'])
    profile_data = github_profile_data(session['sso_github_token'])

    # Retrieve the required details from GitHub User's Profile
    temp_github_id = str(profile_data['id'])
    temp_login = str(profile_data['login'])
    temp_avatar_url = str(profile_data['avatar_url'])

    # Check that GitHub user has a login.
    if len(temp_login) == 0:

        # Clear session data
        if session.get('sso_github_token', False):
            session.pop('sso_github_token', None)

        flash(
            "Sorry, there was an error reading your github username. Try "
            "again.",
            'danger'
        )

        # Send the user back to home page.
        return redirect(url_for('general.home'))

    if (not temp_github_id or
            len(temp_github_id) == 0 or
            temp_github_id == 0):

        # Clear session data
        if session.get('sso_github_token', False):
            session.pop('sso_github_token')

        flash(
            "Sorry, there was an error reading your GitHub ID. Try again.",
            'danger'
        )
        # Send the
        # user back to home page.
        return redirect(url_for('general.home'))

    # Avatar link check - since GitHub manages this endpoint
    # avatar image URL issues should only arise if GitHub updates the way that
    # their users can store their images.
    if 'avatars.githubusercontent.com' not in temp_avatar_url:
        # pass anyway but with no image link.
        temp_avatar_url = ""

    # Create Lists for logic to find a verified email address for the User.
    temp_verified_email = []
    temp_primary = []

    # Find verified emails that were retrieved from the GitHub API.
    for i in email_data:
        if (str(i['verified']) == "True" and
                'noreply.github.com' not in str(i['email'])):

            temp_verified_email.append(str(i['email']))

            if str(i['primary']) == 'True':
                temp_primary.append(str(i['email']))

    # Check that there is a verified_email.
    if len(temp_verified_email) == 0:
        # This account cannot be used for login since no emails are verified.
        if session.get('sso_github_token', False):
            # Pop token remove GitHub Authorization for this token.
            session.pop('sso_github_token')

        flash(
            "Sorry, you cannot register since you have no verified emails "
            "associated with your GitHub account.",
            'danger'
        )

        # Send the user back to home page.
        return redirect(url_for('general.home'))

    # Find GitHub user's primary email or any email that is verified.
    registration_email = temp_primary[0] \
        if len(temp_primary) > 0 else temp_verified_email[0]

    # if ID already exists: then log them in.
    # if other details such as email are already associated but on a
    # different ID, prevent the user from registering and delete their access
    # token. The site requires a unique email address.

    # Check if GitHub ID is already in database
    # if so, refresh their details and log them in.
    try:
        if (db.session.query(exists().where(
                User.github_sso_id == temp_github_id)).scalar()):
            # Find Existing GitHub ID from database.
            existing_user = db.session.query(User).filter(
                User.github_sso_id == temp_github_id).first()

            # Check to make sure the new email address is not registered to
            # another account.
            if (existing_user.github_sso_email != registration_email and
                    db.session.query(exists().where(
                        and_(
                            temp_github_id != User.github_sso_id,
                            or_(
                                registration_email == User.github_sso_email,
                                registration_email == User.google_sso_email,
                                registration_email == User.email
                            ),
                        )
                    ))):
                # Remove GitHub Authorization for this token.
                if session.get('sso_github_token', False):
                    # Store response from GitHub in resp.
                    resp = github_logout(session.get('sso_github_token'))

                    # Check if GitHub provided a successful logout status code.
                    if resp.status_code == 204:
                        # Clear session
                        session.pop('sso_github_token')
                        clear_github_session()

                    flash(
                        "GitHub authorization revoked.",
                        'success'
                    )
                else:
                    flash(
                        "Could not access GitHub Token.",
                        'danger'
                    )
                    # Redirect the
                    # user back to homepage.
                    db.session.close()

                    return redirect(url_for('general.home'))

                flash(
                    "The primary email associated with your GitHub account is "
                    "already registered. Set a different "
                    "primary email address for your GitHub account then try "
                    "again.",
                    'danger'
                )

                db.session.close()

                # Redirect the user back to homepage.
                return redirect(url_for('general.home'))

            # Add session tokens
            session['user_id'] = existing_user.id

            session['sso_github'] = True
            session['sso_github_id'] = existing_user.github_sso_id

            # Check if any details have been changed.
            temp_changed_email = False
            temp_changed_name = False

            temp_changed_avatar = False

            if existing_user.github_sso_email != registration_email:
                # Update Existing Email
                existing_user.github_sso_email = registration_email
                temp_changed_email = True

            if existing_user.github_sso_name != temp_login:
                # Update GitHub Name (Login)
                existing_user.github_sso_name = temp_login
                temp_changed_name = True

            if existing_user.github_sso_image != temp_avatar_url:
                # Update GitHub Avatar URL
                existing_user.github_sso_image = temp_avatar_url
                temp_changed_avatar = True

            # Set session for user on GitHub Login
            session['sso_github_email'] = registration_email
            session['sso_github_name'] = temp_login
            session['sso_github_image'] = existing_user.github_sso_image

            # Finally, commit to database if there were changes.
            if (temp_changed_email or
                    temp_changed_name or
                    temp_changed_avatar):
                db.session.commit()

            flash(
                "You have been logged in as " +
                str(temp_login),
                'success'
            )
            user_check_set_active_profile()

            db.session.close()

            # Send the user back to home page.
            return redirect(url_for('general.home'))

        # User was not found, so
        # Create a new User
        new_user = User(
            github_sso=True,
            github_sso_id=temp_github_id,
            github_sso_email=registration_email,
            github_sso_name=temp_login,
            github_sso_image=temp_avatar_url
        )

        # Add the user to the database.
        db.session.add(new_user)

        # Finally, commit to database
        db.session.commit()

        # Set the session for GitHub Login.
        session['user_id'] = new_user.id

        session['sso_github'] = True

        session['sso_github_id'] = new_user.github_sso_id

        session['sso_github_email'] = new_user.github_sso_email

        session['sso_github_name'] = new_user.github_sso_name

        session['sso_github_image'] = new_user.github_sso_image

        flash(
            "Your GitHub account has been registered with our website.",
            'success'
        )
        db.session.close()
        # Send the
        # user back to home page.
        return redirect(url_for('general.home'))

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.rollback()
        db.session.close()

        # Clear GitHub Session
        if session.get('sso_github_token', False):
            session.pop('sso_github_token', None)

        clear_github_session()

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

        # Clear GitHub Session
        if session.get('sso_github_token', False):
            session.pop('sso_github_token', None)

        clear_github_session()

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

        # Clear GitHub Session
        if session.get('sso_github_token', False):
            session.pop('sso_github_token', None)

        clear_github_session()

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

        # Clear GitHub Session
        if session.get('sso_github_token', False):
            session.pop('sso_github_token', None)

        clear_github_session()

        print(f"Error: {e}")
        flash(
            "There was an error. Try again later.",
            'danger'
        )
        # Redirect the user back to homepage.
        return redirect(url_for('general.home'))


@sso_github_bp.route(
    "/sso_github_logout"
)
def sso_github_logout():
    """
    This route is used to remove a user from GitHub authorization.

    The User Table no longer has any associated details with it and
    all user data will be completely deleted.
    """

    # Check if the user is not logged in.
    if not session.get('user_id', False):
        flash(
            "Sorry, you cannot access this page since you are not logged in.",
            'danger'
        )
        # Send the
        # user back to home page.
        return redirect(url_for('general.home'))

    # Check if GitHub Token is not in session.
    if not session.get('sso_github_token', False):
        flash(
            "You're not authenticated using GitHub.",
            'danger'
        )
        # Send the
        # user back to home page.
        return redirect(url_for('general.home'))

    # Store the response from GitHub Logout in resp.
    resp = github_logout(session.get('sso_github_token'))

    # Check if GitHub did not return a Status Code 204.
    if not resp.status_code == 204:
        flash(
            "Sorry, GitHub didn't allow us to revoke your user token. "
            "Please use their portal to remove our access instead.",
            'danger'
        )

        # Send the user back to home page.
        return redirect(url_for('general.home'))

    session.pop('sso_github_token')

    # now do database operations
    temp_id = session.get('user_id', False)
    if temp_id:
        if db.session.query(exists().where(User.id == int(temp_id))).scalar():
            existing_user = db.session.query(User).filter(
                User.id == int(temp_id)).first()
            db.session.delete(existing_user)
            db.session.commit()

    # Clear Session
    clear_github_session()

    flash(
        "Your GitHub token has been revoked and any associated "
        "details removed from our systems.",
        'success'
    )

    # Send user back to the homepage.
    return redirect(url_for('general.home'))


def check_github_failure(resp):
    """
    Checks if GitHub authentication has failed.
    """
    return 'Bad credentials' == resp.get('message', False)


def github_logout(access_token):
    """
    Access GitHub API and remove app authorization.
    """
    return requests.delete(
        "https://api.github.com/applications/" + sso_github_id + "/token",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {sso_github_secret}",
            "X-GitHub-Api-Version": "2022-11-28"
        },
        auth=HTTPBasicAuth(sso_github_id, sso_github_secret),
        json={'access_token': access_token}
    )


def github_profile_data(access_token):
    """
    Access GitHub API and retrieve profile data
    """
    return (
        requests.get(
            'https://api.github.com/user',
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {access_token}",
                "X-GitHub-Api-Version": "2022-11-28"
            })
        .json()
    )


def github_email_data(access_token):
    """
    Access GitHub API and retrieve emails
    """
    return (
        requests.get(
            'https://api.github.com/user/emails',
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {access_token}",
                "X-GitHub-Api-Version": "2022-11-28"
            })
        .json()
    )


def github_access_token(code):
    """
    Access GitHub API and retrieve an access token used for retrieving data
    such as emails or profile data.
    """
    return (
        requests.post(
            'https://github.com/login/oauth/access_token',
            data={
                'client_id': sso_github_id,
                'client_secret': sso_github_secret,
                'code': code
            },
            headers={
                'Accept': 'application/json'
            })
        .json()
        .get('access_token')
    )


def clear_github_session():
    """
    Clear GitHub Session from server
    This does not include GitHub App Authorization
    GitHub Token does not get cleared.
    """
    if session.get('user_id', False):
        session.pop('user_id', None)

    if session.get('profile_id', False):
        session.pop('profile_id', None)

    if session.get('sso_github_token', False):
        session.pop('sso_github_token', None)

    if session.get('sso_github', False):
        session.pop('sso_github', None)

    if session.get('sso_github_id', False):
        session.pop('sso_github_id', None)

    if session.get('sso_github_email', False):
        session.pop('sso_github_email', None)

    if session.get('sso_github_name', False):
        session.pop('sso_github_name', None)

    if session.get('sso_github_image', False):
        session.pop('sso_github_image', None)


# Development only
@sso_github_bp.route(
    "/sso_github_info"
)
def sso_github_info():
    """
    Store HTML Page to examine later

    This function is here for debugging purposes, if GitHub changes the way that
    they do authorization.

    This shows sensitive data provided by SSO logins so disable during
    production.
    """
    # Check if user is not logged in.
    if not session.get('user_id', False):
        flash(
            "Sorry, you cannot access this page since you are not logged "
            "in.",
            'danger'
        )

        # Redirect user
        # back to homepage.
        return redirect(url_for('general.home'))

    # Check if GitHub Token is in session.
    if not session.get('sso_github_token', False):

        # Check if user is already logged in.
        if session.get('user_id', False):
            flash(
                "You're not logged in through GitHub.",
                'danger')
            # Send user
            # back to home
            return redirect(url_for('general.home'))

        flash(
            "Github account not associated.",
            'danger')
        # Attempt to
        # re-authenticate GitHub
        return redirect(url_for('sso_github.sso_github'))

    # Set profile_data for convenience
    profile_data = github_profile_data(session.get('sso_github_token'))

    # Check for GitHub Failure
    if check_github_failure(profile_data):

        # Clear GitHub Session
        session.pop('sso_github_token')
        clear_github_session()

        # Redirect the user back to GitHub Authentication on failure.
        return redirect(url_for('sso_github.sso_github'))

    return_string = "Login: " + str(profile_data['login']) + "<br/>"

    return_string += "ID: " + str(profile_data['id']) + "<br/>"

    return_string += ("Avatar URL: " + str(profile_data['avatar_url']) +
                      "<br/>")

    return_string += ("Avatar: <br/> <img src=" +
                      str(profile_data['avatar_url'])) + " /><br/><hr/>"

    """
    return_string = str(profile_data) + "<br/>"
    for key, item in zip(profile_data.keys(), profile_data.values()):
        return_string += str(key) + ": " + str(item) + "<br/>"
    """

    return_string += "SELECTED EMAILS<hr/>"

    # Grab Email Data
    email_data = github_email_data(session['sso_github_token'])

    # Iterate through email data and get usable emails.
    for i in email_data:
        if (str(i['verified']) == "True" and
                'noreply.github.com' not in str(i['email'])):
            return_string += "Email: " + str(i['email']) + "<br/>"
            return_string += "Verified: " + str(i['verified']) + "<br/>"
            return_string += ("Primary: " + str(i['primary']) +
                              "<br/><hr/>")
    """
        Multiple entries for Email
        noreply.github.com (private email not allowed)
        anything else:
            Verified is True, Primary is True, or any other Verified Email.
    """
    """
    return_string += str(email_data) + "<br/>"
    for key, item in enumerate(email_data):
        return_string += str(key) + ": " + str(item) + "<br/>"
    """

    # Return the string with GitHub Profile Data that was accessed.
    return return_string


# Development only
# @sso_github_bp.route("/sso_github_check")
def sso_github_check():
    """
    This function is here for debugging purposes, if GitHub changes the way that
    they do authorization.

    This shows sensitive data provided by SSO logins so disable during
    production.
    """

    # Check if user is already logged in through Email.
    if session.get('email', False):
        flash(
            "Sorry, you cannot access this page since you are already "
            "logged in through Email.",
            'danger'
        )

        # Send the User back to the homepage.
        return redirect(
            url_for(
                'general.home'
            )
        )

    # Check if user is already logged in through Google.
    if session.get('sso_google', False):
        flash(
            "Sorry, you cannot access this page since you are already "
            "logged in through Google.",
            'danger'
        )

        # Send the User back to the homepage.
        return redirect(
            url_for(
                'general.home'
            )
        )

    # Check if GitHub token is found
    if not session.get('sso_github', False):
        flash(
            "Sorry, you cannot access this page since you are not logged "
            "in through GitHub.",
            'danger'
        )

        # Send the User back to the homepage.
        return redirect(url_for('general.home'))

    resp = github_profile_data(session.get('sso_github_token'))

    # Check if token authentication failure
    if check_github_failure(resp):
        # Remove the token object
        session.pop('sso_github_token')
        clear_github_session()

        return redirect(url_for('sso_github.sso_github'))

    # Finally return the response that was sent from GitHub
    return str(resp)
