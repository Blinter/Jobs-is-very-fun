"""
Email
JWT usage and sending emails
Routes for accepting JWT tokens, displays form after user verifies their
email, then POST data.
"""
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    session
)

from jwt import exceptions
from datetime import datetime, UTC, timedelta
from flask_mailman import EmailMessage
from extensions_keys import jwt_keys
from extensions_user import get_username_from_email
from user_jobs.forms.CreateUserFromVerifiedEmail import (
    CreateUserFromVerifiedEmail
)

from user_jobs.forms.ResetPasswordFromVerifiedEmail import (
    ResetPasswordFromVerifiedEmail
)

from secrets_jobs.credentials import (
    mail_server_mail_from,
    website_return_url,
    google_recaptcha_v2_key,
    google_recaptcha_v2_enabled
)

email_bp = Blueprint(
    'email',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/email'
)


def send_verification_email(user_email):
    """
    Send User Verification Email
    Creates a JWT token then sends this token to the user's provided email
    address.
    """
    current_date_time_utc = datetime.now(UTC)
    token = jwt_keys.sign_payload(
        payload={
            'sub': user_email,
            'exp': (current_date_time_utc + timedelta(minutes=15)).timestamp(),
            'nbf': (current_date_time_utc + timedelta(seconds=3)).timestamp(),
            'iat': current_date_time_utc.timestamp(),
            'iss': website_return_url,
            'aud': mail_server_mail_from
        }
    )

    # Create the email
    email = EmailMessage(
        subject="Jobs.is-very.fun | New Sign Up Verification",
        body=render_template(
            "email/outgoing_email_verification.html",
            token=token,
            new_email=user_email,
            website_return_url=website_return_url
        ),
        from_email=mail_server_mail_from,
        reply_to=[mail_server_mail_from],
        to=[user_email]
    )

    # Set content type for the email to HTML
    email.content_subtype = "html"

    # Send the Email
    email.send()


def send_password_reset_email(user_email):
    """
    Send User Password Reset Token
    Creates a JWT token then sends this token to the user's provided email
    address.
    """
    current_date_time_utc = datetime.now(UTC)
    token = jwt_keys.sign_payload(
        payload={
            'sub': user_email,
            'exp': (current_date_time_utc + timedelta(minutes=15)).timestamp(),
            'nbf': (current_date_time_utc + timedelta(seconds=3)).timestamp(),
            'iat': current_date_time_utc.timestamp(),
            'iss': website_return_url,
            'aud': mail_server_mail_from
        }
    )

    # Create the email
    email = EmailMessage(
        subject="Jobs.is-very.fun | Password Reset Request",
        body=render_template(
            "email/outgoing_email_forgot_password.html",
            token=token,
            user_email=user_email,
            website_return_url=website_return_url
        ),
        from_email=mail_server_mail_from,
        reply_to=[mail_server_mail_from],
        to=[user_email],
    )

    # Set content type for the email to HTML
    email.content_subtype = "html"

    # Send the Email
    email.send()


@email_bp.route("/email_verification/", defaults={'v': None})
@email_bp.route("/email_verification/<string:v>")
def email_verification(v):
    """
    Email Verification
    A new user can verify the token that was sent to their email address.
    """
    if session.get('user_id', False):
        flash(
            "Sorry, you cannot access this page since you are already "
            "logged in.",
            'danger'
        )

        # Send user back to beginning of registration process.
        return redirect(url_for('general.home'))

    if not v or len(v) == 0:
        flash(
            "You need a token that was sent from the email. Please try "
            "registration again.",
            'danger'
        )

        # Send user back to beginning of registration process.
        return redirect(url_for('user.register'))

    try:
        # Decode the payload from the token that was sent to the user.
        payload = jwt_keys.get_payload(payload=v)

        # Debug JWT
        """
        exp_time = datetime.fromtimestamp(payload["exp"], tz=UTC)
        nbf_time = datetime.fromtimestamp(payload["nbf"], tz=UTC)
        iat_time = datetime.fromtimestamp(payload["iat"], tz=UTC)

        issuer = payload["iss"]
        audience = payload["aud"]
        print("User Email:", user_email)
        print("Expiration Time:", exp_time)
        print("Not Before Time:", nbf_time)
        print("Issued At Time:", iat_time)

        print("Issuer:", issuer)
        print("Audience:", audience)
        if exp_time < datetime.now(UTC):
            print("Token has expired.")
        else:
            print("Token is still valid.")

        if nbf_time > datetime.now(UTC):
            print("Token is not yet valid.")
        else:
            print("Token was provided during valid time-frame.")
        """

        # use email_registration to store the email that was read from the
        # token.
        session['email_registration'] = payload["sub"]

        # Extra state for user
        session['email_state'] = True

        # Everything is set, send the create user form.
        return render_template(
            "user/verified_email_registration_form.html",
            form=CreateUserFromVerifiedEmail(),
            user_verified_email=str(session.get('email_registration')),
            check_captcha=google_recaptcha_v2_enabled,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    except exceptions.DecodeError:
        flash(
            "Couldn't decode the token, please try registration again.",
            'danger'
        )

        # Reset the session states
        if session.get('email_state', False):
            session.pop('email_state', None)

        if session.get('email_registration', False):
            session.pop('email_registration', None)

        # Send user back to beginning of registration process.
        return redirect(url_for('user.register'))

    except exceptions.ExpiredSignatureError:
        flash(
            "Verification Expired, please try registration again.",
            'danger'
        )

        # Reset the session states
        if session.get('email_state', False):
            session.pop('email_state', None)

        if session.get('email_registration', False):
            session.pop('email_registration', None)

        # Send user back to beginning of registration process.
        return redirect(url_for('user.register'))


@email_bp.route("/reset_password/", defaults={'v': None})
@email_bp.route("/reset_password/<string:v>")
def reset_password(v):
    """
    Reset Password
    An existing user can verify the token that was sent to their own email
    address in order to reset a password associated with it.
    """
    if session.get('user_id', False):
        flash(
            "Sorry, you cannot access this page since you are already "
            "logged in.",
            'danger'
        )

        # Send user back to home page.
        return redirect(url_for('general.home'))

    if not v or len(v) == 0:
        flash("You need a token that was sent from the email. Please try "
              "the forgot password form again.",
              'danger'
              )

        # Send user back to forgot password form to try again.
        return redirect(url_for('user.forgot_password'))

    try:
        payload = jwt_keys.get_payload(payload=v)

        # Save the email state
        session['email_state'] = payload["sub"]

        # get_username_from_email selects the username from database based on
        # a provided email.
        # Retrieve username from email and set extra state for username
        session['username_state'] = get_username_from_email(
            session.get('email_state', None))

        # Make sure that email is valid.
        if not session.get('email_state', False):
            flash(
                "Sorry, the email could not be found.",
                'danger'
            )

            # Send user back to forgot password form to try again.
            return redirect(url_for('user.forgot_password'))

        # Make sure that username is valid.
        if (not session.get('username_state', False) or
                session.get('username_state', None) is None):

            flash(
                "Sorry, the username could not longer be found based on the "
                "email you provided.",
                'danger'
            )

            # Send user back to forgot password form to try again.
            return redirect(url_for('user.forgot_password'))

        # All checks passed, now provide the reset password form.
        return render_template(
            "user/reset_password_form.html",
            form=ResetPasswordFromVerifiedEmail(),
            email=session.get('email_state'),
            username=session.get('username_state'),
            check_captcha=google_recaptcha_v2_enabled,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    except exceptions.DecodeError:
        flash(
            "Couldn't decode the token, please try the forgot password form "
            "again.",
            'danger'
        )

        # Remove the session objects
        if session.get('username_state', False):
            session.pop('username_state', None)

        if session.get('email_state', False):
            session.pop('email_state', None)

        # Send user back to forgot password form to try again.
        return redirect(url_for('user.forgot_password'))

    except exceptions.ExpiredSignatureError:
        flash(
            "Verification Expired, please try registration again.",
            'danger'
        )

        # Remove the session objects
        if session.get('username_state', False):
            session.pop('username_state', None)

        if session.get('email_state', False):
            session.pop('email_state', None)

        # Send user back to forgot password form to try again.
        return redirect(url_for('user.forgot_password'))
