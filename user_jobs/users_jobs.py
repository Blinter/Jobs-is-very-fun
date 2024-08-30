from flask import (
    request,
    Blueprint,
    session,
    redirect,
    flash,
    url_for,
    render_template
)

from user_jobs.forms.ChangePassword import ChangePassword
from user_jobs.forms.SingleEmailForm import SingleEmailForm

from user_jobs.forms.CreateUserFromVerifiedEmail import (
    CreateUserFromVerifiedEmail
)

from user_jobs.forms.ResetPasswordFromVerifiedEmail import (
    ResetPasswordFromVerifiedEmail
)

from user_jobs.forms.LoginEmailOrPassword import LoginEmailOrPassword
from secrets_jobs.credentials import (
    mail_server_mail_from,
    google_recaptcha_v2_key,
    google_recaptcha_v2_enabled
)

from models.postgres.user import User
from sqlalchemy import exists
from email_jobs.email_jobs import (
    send_verification_email,
    send_password_reset_email
)

from extensions_sql import db
from extensions_user import (
    google_verify_recaptcha,
    clear_email_session,
    get_authenticated_user_name,
    get_delete_link
)

from extensions_profiles import user_check_set_active_profile


user_bp = Blueprint(
    'user',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/user'
)


@user_bp.route(
    "/user_dashboard"
)
def user_dashboard():
    """
    User Dashboard to display profiles and other user actions.
    """
    return render_template(
        "user/user_dashboard.html",
        user=get_authenticated_user_name(),
        email=session.get('email'),
        delete_link=get_delete_link(),
    )


@user_bp.route(
    "/login",
    methods=["GET", "POST"]
)
def login():
    """
    Login user using email (GET, POST)
    """

    # Check if the User is already logged in.
    if session.get('user_id', False):
        flash(
            "Sorry, you cannot access this page since you are already "
            "logged in.",
            'danger'
        )

        # Send the logged-in user back to the homepage.
        return redirect(url_for('general.home'))

    form = LoginEmailOrPassword()

    # Validate form
    if not form.validate_on_submit():
        # Debug Only
        """"
        for field, errors in form.errors.items():
            for error in errors:
                print(f"Error for field '{field}': {error}")
        """

        # Allow user to retry the login form again.
        return render_template(
            "user/user_or_email_login_form.html",
            form=form,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Skip if Recaptcha is disabled
    check_captcha = google_recaptcha_v2_enabled

    recaptcha = request.form.get('g-recaptcha-response', False)

    # Validate captcha response from Google
    if (check_captcha and
            (not recaptcha or
             not google_verify_recaptcha(recaptcha))):
        flash(
            "You need to verify the recaptcha. Try again.",
            'danger'
        )

        # Allow user to retry the login form again.
        return render_template(
            "user/user_or_email_login_form.html",
            form=form,
            check_captcha=check_captcha,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Form validation checks passed.

    # Set temp_user_or_email and temp_password for convenience.
    temp_user_or_email = request.form.get('email_or_username', False)
    temp_password = request.form.get('password', False)

    # Check submitted form data

    # Check username and password are set.
    if not temp_user_or_email or not temp_password:
        flash(
            "Email and Username or Password must be submitted.",
            'danger'
        )

        # Allow user to retry the login form again.
        return render_template(
            "user/user_or_email_login_form.html",
            form=form,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Check that Username or Email are acceptable length.
    if (len(temp_user_or_email) < 3 or
            len(temp_user_or_email) > 128):
        flash(
            "Email or Username must be between 3 and 128 "
            "characters long. Try a valid input length.",
            'danger'
        )

        # Allow user to retry the login form again.
        return render_template(
            "user/user_or_email_login_form.html",
            form=form,
            check_captcha=check_captcha,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Check password is an acceptable length.
    if len(temp_password) < 5 or len(temp_password) > 70:
        flash(
            "Password must be between 5 and 70 characters",
            'danger'
        )

        # Allow user to retry the login form again.
        return render_template(
            "user/user_or_email_login_form.html",
            form=form,
            check_captcha=check_captcha,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Data length checks passed.
    # Check Database and complete authentication

    # Validate if username or email provided and
    # Check if username or email exists in database
    if (not db.session.query(exists().where(
            User.username == temp_user_or_email)).scalar()
            if temp_user_or_email.find('@') == -1 else
            not db.session.query(exists().where(
                User.email == temp_user_or_email)).scalar()):
        flash(
            "Sorry, the email address or username you provided is not in "
            "our database.",
            'danger'
        )

        # Allow user to retry the login form again.
        return render_template(
            "user/user_or_email_login_form.html",
            form=form,
            check_captcha=check_captcha,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Select the user, then verify the password.
    existing_user = (
        db.session.query(User).filter(
            User.username == temp_user_or_email
            if temp_user_or_email.find('@') == -1 else
            User.email == temp_user_or_email).first()
    )

    # Verify login
    if not existing_user.authenticate(temp_password):
        flash(
            "Sorry, the password your provided is not valid. This has been "
            "logged.",
            'danger'
        )

        # Allow user to retry the login form again.
        return render_template(
            "user/user_or_email_login_form.html",
            form=form,
            check_captcha=check_captcha,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # All checks passed

    # Set session objects
    session['user_id'] = existing_user.id

    session['username'] = existing_user.username
    session['email'] = existing_user.email
    
    # Look for a profile in the database to set their active profile.

    flash(
        'You are successfully logged in as ' + str(existing_user.username),
        'success'
    )
    user_check_set_active_profile()
    db.session.close()

    # Send the logged-in user back to homepage.
    return redirect(url_for('general.home'))


@user_bp.route(
    "/complete_register_by_email",
    methods=["POST"]
)
def complete_register_by_email():
    """
    End of user registration process: User has clicked on verification link,
    and has input data for registration.
    """

    # Check if username is already logged in.
    if session.get('user_id', False):
        flash(
            "Sorry, you cannot access this page since you are already "
            "logged in.",
            'danger'
        )

        # Send the user back to the homepage.
        return redirect(url_for('general.home'))

    # Check registration states if they exist.
    if (not session.get('email_state', False) or
            not session.get('email_registration', False)):

        flash(
            "Sorry, you cannot access this page since you have not "
            "started an email sign-up process.",
            'danger'
        )

        # Send the user back to the homepage.
        return redirect(url_for('general.home'))

    # Set temp_email for convenience
    temp_email = session.get('email_registration', False)

    # Check email registration session
    if not temp_email:
        flash(
            "Sorry, your session timed out. Please attempt to "
            "register again.",
            'danger'
        )

        # Clear registration session objects.
        if session.get('email_state', False):
            session.pop('email_state', None)

        if session.get('email_registration', False):
            session.pop('email_registration', None)

        # Send the user back to registration to try again.
        return redirect(url_for('user.register'))

    # Form Validation
    form = CreateUserFromVerifiedEmail()

    # Check if form validates successfully.
    if not form.validate_on_submit():

        # Debug Only

        for field, errors in form.errors.items():
            for error in errors:
                print(f"Error for field '{field}': {error}")

        # Allow the user to retry the form.
        return render_template(
            "user/verified_email_registration_form.html",
            form=form,
            user_verified_email=session.get('email_registration'),
            check_captcha=google_recaptcha_v2_enabled,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Skip if Recaptcha is disabled
    check_captcha = google_recaptcha_v2_enabled

    # Check recaptcha
    recaptcha = request.form.get('g-recaptcha-response', False)

    # Check if recaptcha is successful.
    if (check_captcha and
            (not recaptcha or
             not google_verify_recaptcha(recaptcha))):
        flash(
            "You need to verify the recaptcha. Try again.",
            'danger'
        )

        # Allow the user to retry the form.
        return render_template(
            "user/verified_email_registration_form.html",
            form=form,
            user_verified_email=session.get('email_registration'),
            check_captcha=check_captcha,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Set temp_user for convenience
    temp_user = request.form.get('username', False)

    # Check that username is provided from the form.
    if not temp_user:
        flash(
            "You need to input a username. Try again.",
            'danger'
        )

        # Allow the user to retry the form if a username is not provided.
        return render_template(
            "user/verified_email_registration_form.html",
            form=form,
            user_verified_email=session.get('email_registration'),
            check_captcha=check_captcha,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Check username length
    if (len(temp_user) < 3 or
            len(temp_user) > 20):
        flash(
            "Username must be between 3 and 20 characters",
            'danger'
        )

        # Allow the user to retry the form if the username length is invalid.
        return render_template(
            "user/verified_email_registration_form.html",
            form=form,
            user_verified_email=session.get('email_registration'),
            check_captcha=check_captcha,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Check if username doesn't contain an @ symbol.
    if str(temp_user).find('@') != -1:
        flash(
            "Username cannot contain an @ symbol.",
            'danger'
        )

        # Allow the user to retry a different username.
        return render_template(
            "user/verified_email_registration_form.html",
            form=form,
            user_verified_email=session.get('email_registration'),
            check_captcha=check_captcha,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Check password from form
    temp_password = request.form.get('password', False)
    if not temp_password:
        flash(
            "You need to input a password. Try again.",
            'danger'
        )

        # Allow the user to try submitting a password.
        return render_template(
            "user/verified_email_registration_form.html",
            form=form,
            user_verified_email=session.get('email_registration'),
            check_captcha=check_captcha,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Input length validation
    # Additional email input length validation
    if (len(str(temp_email)) < 6 or
            len(str(temp_email)) > 128):
        flash(
            "Email must be between 6 and 128 characters long. "
            "Your session cannot continue. Try a different email address.",
            'danger'
        )

        if session.get('email_registration', False):
            session.pop('email_registration', None)

        if session.get('email_state', False):
            session.pop('email_state', None)

        # Send the user back to the registration form.
        return redirect(url_for('user.register'))

    # Additional password input length validation
    if (len(temp_password) < 5 or
            len(temp_password) > 70):
        flash(
            "Password must be between 5 and 70 characters",
            'danger'
        )

        # Allow the user to try a different password
        return render_template(
            "user/verified_email_registration_form.html",
            form=form,
            user_verified_email=session.get('email_registration'),
            check_captcha=check_captcha,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Check for existing username
    if db.session.query(exists().where(temp_user == User.username)).scalar():
        flash(
            "This username already exists. Try again.",
            'danger'
        )

        # Allow the user to try a different username.
        return render_template(
            "user/verified_email_registration_form.html",
            form=form,
            user_verified_email=session.get('email_registration'),
            check_captcha=check_captcha,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Check for existing email
    if (db.session.query(exists().where(
            temp_email == User.github_sso_email or
            temp_email == User.google_sso_email or
            temp_email == User.email)).scalar()):
        flash(
            "Sorry, the email address has already been registered. "
            "Try a different email address.",
            'danger'
        )

        # Clear the session
        if session.get('email_registration', False):
            session.pop('email_registration', None)

        if session.get('email_state', False):
            session.pop('email_state', None)

        # Redirect the user back to the registration form.
        return redirect(url_for('user.register'))

    # All checks completed

    # Create a new user object
    new_user = User(
        username=temp_user,
        email=temp_email,
        encrypted_password=temp_password
    )

    # Encrypt password
    new_user.encrypt_password()

    # Add the new user to the session.
    db.session.add(new_user)

    # Commit to database
    db.session.commit()

    # Set the session objects upon successful commit.
    session['user_id'] = new_user.id
    session['username'] = new_user.username
    session['email'] = new_user.email

    db.session.close()

    # Clear registration session objects.
    if session.get('email_registration', False):
        session.pop('email_registration', None)

    if session.get('email_state', False):
        session.pop('email_state', None)

    flash(
        "Account successfully registered!",
        'success'
    )

    # User is logged in, send back to the home page.
    return redirect(url_for('general.home'))


@user_bp.route(
    "/complete_reset_by_email",
    methods=["POST"]
)
def complete_reset_by_email():
    """
    Email Password Reset
    End of user reset password process:
        User has clicked on verification link,
        and has input data for resetting their password.

    email_state is used for holding the email value
    username_state is used for holding the username value
    """

    # Check if user is already logged in.
    if session.get('user_id', False):

        flash(
            "Sorry, you cannot access this page since you are already "
            "logged in.",
            'danger'
        )

        # Send user back to homepage
        return redirect(url_for('general.home'))

    # Check if User has reset session states.
    if (not session.get('username_state', False) or
            not session.get('email_state', False)):
        flash(
            "Sorry, you cannot access this page since you have not "
            "started an email reset password process.",
            'danger'
        )

        # Redirect the user back to the forgot password form to retry.
        return redirect(url_for('user.forgot_password'))

    # State checks have been passed

    # Set temp_email and temp_user for convenience
    temp_email = session.get('email_state', False)
    temp_user = session.get('username_state', False)

    # Check session has not timed out
    if (not temp_email or
            not temp_user):
        flash(
            "Sorry, your session timed out. Please attempt to "
            "register again.",
            'danger'
        )

        # Clear session objects.
        if session.get('username_state', False):
            session.pop('username_state', None)

        if session.get('email_state', False):
            session.pop('email_state', None)

        # Redirect the user back to the forgot password form to retry.
        return redirect(url_for('user.forgot_password'))

    # Check email length again
    if (len(str(temp_email)) < 6 or
            len(str(temp_email)) > 128):
        flash(
            "Unfortunately, Email must be between 6 and 128 "
            "characters long. Try the process again.",
            'danger'
        )

        # Clear session state
        if session.get('username_state', False):
            session.pop('username_state', None)

        if session.get('email_state', False):
            session.pop('email_state', None)

        # Redirect the user back to the forgot password form to retry.
        return redirect(url_for('user.forgot_password'))

    # Check username length
    if (len(str(temp_user)) < 3 or
            len(str(temp_user)) > 20):
        flash(
            "Username must be between 3 and 20 characters",
            'danger'
        )

        # Clear session state
        if session.get('username_state', False):
            session.pop('username_state', None)

        if session.get('email_state', False):
            session.pop('email_state', None)

        # Redirect the user back to the forgot password form to retry.
        return redirect(url_for('user.forgot_password'))

    # Check username does not contain an @ symbol
    if str(temp_user).find('@') != -1:
        flash(
            "Username cannot contain an @ symbol.",
            'danger'
        )

        # Clear session state
        if session.get('username_state', False):
            session.pop('username_state', None)

        if session.get('email_state', False):
            session.pop('email_state', None)

        # Redirect the user back to the forgot password form to retry.
        return redirect(url_for('user.forgot_password'))

    # Check email contains an @ symbol
    if str(temp_email).find('@') == -1:
        flash(
            "Email must contain an @ symbol.",
            'danger'
        )

        # Clear session state
        if session.get('username_state', False):
            session.pop('username_state', None)

        if session.get('email_state', False):
            session.pop('email_state', None)

        # Redirect the user back to the forgot password form to retry.
        return redirect(url_for('user.forgot_password'))

    form = ResetPasswordFromVerifiedEmail()

    # Skip if Recaptcha is disabled
    check_captcha = google_recaptcha_v2_enabled

    recaptcha = request.form.get('g-recaptcha-response', False)
    if (check_captcha and (
            not recaptcha or
            not google_verify_recaptcha(recaptcha))):
        flash(
            "You need to verify the recaptcha. Try again.",
            'danger'
        )

        # Allow the user to retry the form.
        return render_template(
            "user/reset_password_form.html",
            form=form,
            username=session.get('username_state'),
            email=session.get('email_state'),
            check_captcha=check_captcha,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    if not form.validate_on_submit():
        # Debug Only
        """
        for field, errors in form.errors.items():
            for error in errors:
                print(f"Error for field '{field}': {error}")
        """

        # Allow the user to retry the form.
        return render_template(
            "user/reset_password_form.html",
            form=form,
            username=session.get('username_state'),
            email=session.get('email_state'),
            check_captcha=check_captcha,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    temp_password = request.form.get('password', False)

    temp_password_verify = request.form.get('password_verify', False)

    # Check that both passwords were sent.
    if (not temp_password or
            not temp_password_verify):
        flash(
            "You need to input a password. Try again.",
            'danger'
        )

        # Allow the user to retry the form if password not supplied.
        return render_template(
            "user/reset_password_form.html",
            form=form,
            username=session.get('username_state'),
            email=session.get('email_state'),
            check_captcha=check_captcha,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Check password lengths are within length.
    if (len(str(temp_password)) < 5 or
            len(str(temp_password_verify)) < 5 or
            len(str(temp_password)) > 70 or
            len(str(temp_password_verify)) > 70):
        flash(
            "Password must be between 5 and 70 characters",
            'danger'
        )

        # Allow the user to retry the form if password not valid length.
        return render_template(
            "user/reset_password_form.html",
            form=form,
            username=session.get('username_state'),
            email=session.get('email_state'),
            check_captcha=check_captcha,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Check passwords are equal
    if str(temp_password) != str(temp_password_verify):
        flash(
            "Passwords are not the same. Please check your input.",
            'danger'
        )

        # Allow the user to retry the form if passwords are not equal.
        return render_template(
            "user/reset_password_form.html",
            form=form,
            username=session.get('username_state'),
            email=session.get('email_state'),
            check_captcha=check_captcha,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Input Data checks passed
    # Find the account by checking the email and username.
    # Data length checks passed.

    # Validate if username or email provided and
    # Check if username or email exists in database
    if (not db.session.query(exists().where(
            User.username == str(temp_user) and
            User.email == str(temp_email))).scalar()):
        flash(
            "Sorry, the email address or username that was associated"
            " with your reset request is no longer in our database. "
            "Try again.",
            'danger'
        )

        # Clear session state
        if session.get('username_state', False):
            session.pop('username_state', None)

        if session.get('email_state', False):
            session.pop('email_state', None)

        # Redirect the user back to the forgot password form to retry.
        return redirect(url_for('user.forgot_password'))

    # Select the user, then reset the password.
    existing_user = (
        db.session.query(User).filter(
            User.username == str(temp_user) and
            User.email == str(temp_email)).first()
    )

    # Check if existing password validates first before needing to commit.
    # no log method used
    if existing_user.authenticate_no_log(str(temp_password)):
        flash(
            "New Password must not be the same as the existing password.",
            'danger'
        )

        # Allow the user to input a different password if they supplied the
        # same password that was stored.
        return render_template(
            "user/reset_password_form.html",
            form=form,
            username=session.get('username_state'),
            email=session.get('email_state'),
            check_captcha=check_captcha,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Set new Password
    existing_user.encrypted_password = str(temp_password)

    # Encrypt password
    existing_user.encrypt_password()

    # Finally, commit to database and set session objects.
    db.session.commit()

    # Set session objects.
    session['user_id'] = existing_user.id

    session['username'] = existing_user.username
    session['email'] = existing_user.email

    user_check_set_active_profile()

    db.session.close()

    # Clear password reset session objects.
    if session.get('username_state', False):
        session.pop('username_state', None)

    if session.get('email_state', False):
        session.pop('email_state', None)

    flash(
        "Account password successfully reset! You are now logged in.",
        'success'
    )

    # User is logged in, now send them back to the home page.
    return redirect(url_for('general.home'))


@user_bp.route(
    "/register",
    methods=["GET", "POST"]
)
def register():
    """
    Sends a verification email to the user's provided email address
    Checks form input and captcha verification.
    Checks if the email is not already in the database.
    """

    # Check if user has already signed in
    if session.get('user_id', False):
        flash(
            "Sorry, you cannot access this page since you are already "
            "logged in.",
            'danger'
        )

        # Send the user back to home page
        return redirect(url_for('general.home'))

    # User may get locked out if they are in the process of verifying an
    # email but decide not to complete their registration.

    """
    if not session.get('email_state', False):
        flash(
        "Sorry, you cannot access this page since you are in the "
              "process of verifying an email.", 'danger')
        return redirect(url_for('general.home'))
    """

    # Form and validation check
    form = SingleEmailForm()
    if not form.validate_on_submit():
        # Debug Only
        """
        for field, errors in form.errors.items():
            for error in errors:
                print(f"Error for field '{field}': {error}")
        """

        # Allow the user to retry registration after checking form errors.
        return render_template(
            "user/user_registration_form.html",
            form=form,
            check_captcha=google_recaptcha_v2_enabled,
            recaptcha_v2_client=google_recaptcha_v2_key,
            send_email_from=mail_server_mail_from
        )

    # Skip if Recaptcha is disabled
    check_captcha = google_recaptcha_v2_enabled

    recaptcha = request.form.get('g-recaptcha-response', False)

    # Check for Recaptcha failed response
    if (check_captcha and
            (not recaptcha or
             not google_verify_recaptcha(recaptcha))):
        flash(
            "You need to verify the recaptcha. Try again.",
            'danger'
        )

        # Allow the user to retry registration.
        return render_template(
            "user/user_registration_form.html",
            form=form,
            recaptcha_v2_client=google_recaptcha_v2_key,
            send_email_from=mail_server_mail_from
        )

    # Temporary email variable for convenience
    temp_email = str(form.email.data)

    # Check email is set
    if not temp_email:
        flash(
            "Sorry, your email is not valid.",
            'danger'
        )

        # Send user back to registration form.
        return redirect(url_for('user.register'))

    # Check email length
    if (len(temp_email) < 6 or
            len(temp_email) > 128):
        flash(
            "Email must be between 6 and 128 "
            "characters long. Your session cannot continue. "
            "Try a different email address.",
            'danger'
        )

        # Send user back to registration form.
        return redirect(url_for('user.register'))

    # Check that email contains an @ Symbol
    if str(temp_email).find('@') == -1:
        flash(
            "Email must contain an @ symbol.",
            'danger'
        )

        # Send user back to registration form.
        return redirect(url_for('user.register'))

    # Check if Email is already in database
    if db.session.query(exists().where(
            temp_email == User.github_sso_email or
            temp_email == User.google_sso_email or
            temp_email == User.email)).scalar():
        flash(
            "Sorry, this email address has already been "
            "registered with us.",
            'danger'
        )

        return redirect(url_for('user.register'))

    # Finally send verification email
    send_verification_email(temp_email)

    flash(
        "Please check your email. The link expires in 15 "
        "minutes. It may show up in your spam folder.",
        'success'
    )

    # Redirect back to home page
    return redirect(url_for('general.home'))


@user_bp.route(
    "/forgot_password",
    methods=["GET", "POST"]
)
def forgot_password():
    """
    Reset password using a user provided email address. (GET, POST)
    This form emails a forgot password link to the User.
    """

    # Check if the User is already logged in.
    if session.get('user_id', False):
        flash(
            "Sorry, you cannot access this page since you are already "
            "logged in.",
            'danger'
        )

        # Send the user back to the homepage.
        return redirect(url_for('general.home'))

    form = SingleEmailForm()

    # Check that form validates successfully.
    if not form.validate_on_submit():
        # Debug information only
        """
        for field, errors in form.errors.items():
            for error in errors:
                print(f"Error for field '{field}': {error}")
        """

        # Allow user to retry the forgot password form again.
        return render_template(
            "user/user_forgot_password_form.html",
            form=form,
            recaptcha_v2_client=google_recaptcha_v2_key,
            send_email_from=mail_server_mail_from
        )

    # Skip if Recaptcha is disabled
    check_captcha = google_recaptcha_v2_enabled

    # Check Recaptcha form data.
    recaptcha = request.form.get('g-recaptcha-response', False)

    # Check if recaptcha validates successfully.
    if (check_captcha and
            (not recaptcha or
             not google_verify_recaptcha(recaptcha))):
        flash(
            "You need to verify the recaptcha. Try again.",
            'danger'
        )

        # Allow user to retry the forgot password form again.
        return render_template(
            "user/user_forgot_password_form.html",
            form=form,
            recaptcha_v2_client=google_recaptcha_v2_key,
            send_email_from=mail_server_mail_from
        )

    # Initial Form checks passed.

    # Set temp_email for convenience.
    temp_email = request.form.get('email', False)

    # Check form input data here

    # Check if temp_email is submitted with the form.
    if not temp_email:
        flash(
            "An email must be submitted.",
            'danger'
        )

        # Allow user to retry the forgot password form again.
        return render_template(
            "user/user_forgot_password_form.html",
            form=form,
            recaptcha_v2_client=google_recaptcha_v2_key,
            send_email_from=mail_server_mail_from
        )

    # Check that the provided email is within acceptable length.
    if (len(temp_email) < 6 or
            len(temp_email) > 128):
        flash(
            "Email must be between 6 and 128 "
            "characters long. Try a valid input length.",
            'danger'
        )

        # Allow user to retry the forgot password form again.
        return render_template(
            "user/user_forgot_password_form.html",
            form=form,
            recaptcha_v2_client=google_recaptcha_v2_key,
            send_email_from=mail_server_mail_from
        )

    # Data length checks passed.

    # Check if email exists in database
    if not (db.session.query(exists().where(
            User.email == temp_email)).scalar()):
        flash(
            "Sorry, the email address you provided is not in our database.",
            'danger'
        )

        # Allow user to retry the forgot password form again.
        return render_template(
            "user/user_forgot_password_form.html",
            form=form,
            recaptcha_v2_client=google_recaptcha_v2_key,
            send_email_from=mail_server_mail_from
        )

    # All checks passed

    # Finally send password reset email
    send_password_reset_email(temp_email)

    flash(
        "Please check your email. The link expires in 15 "
        "minutes. It may show up in your spam folder.",
        'success'
    )

    # Redirect back to home page
    return redirect(url_for('general.home'))


@user_bp.route(
    "/change_password",
    methods=["GET", "POST"]
)
def change_password():
    """
    Change a password for a logged-in user. (GET, POST)
    This form changes a password for an already existing user.
    """

    # Check if the User is not logged in.
    if not session.get('user_id', False):
        flash(
            "Sorry, you cannot access this page since you are not "
            "logged in.",
            'danger'
        )

        # Send the user back to the homepage.
        return redirect(url_for('general.home'))

    # Check if the User logged in through email.
    if not session.get('email', False):
        flash(
            "Sorry, you cannot access this page since you are not "
            "logged in through email.",
            'danger'
        )

        # Send the user back to the homepage.
        return redirect(url_for('general.home'))

    form = ChangePassword()

    # Check that form validates successfully.
    if not form.validate_on_submit():
        # Debug information only
        """
        for field, errors in form.errors.items():
            for error in errors:
                print(f"Error for field '{field}': {error}")
        """

        # Allow user to retry the forgot password form again.
        return render_template(
            "user/change_password_form.html",
            form=form,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Skip if Recaptcha is disabled
    check_captcha = google_recaptcha_v2_enabled

    # Check Recaptcha form data.
    recaptcha = request.form.get('g-recaptcha-response', False)

    # Check if recaptcha validates successfully.
    if (check_captcha and
            (not recaptcha or
             not google_verify_recaptcha(recaptcha))):
        flash(
            "You need to verify the recaptcha. Try again.",
            'danger'
        )

        # Allow user to retry the forgot password form again.
        return render_template(
            "user/change_password_form.html",
            form=form,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Initial Form checks passed.

    # Set variables here for convenience
    previous_password = request.form.get('password_previous', False)
    temp_password = request.form.get('password', False)
    temp_password_verify = request.form.get('password_verify', False)

    # Check that all three password forms were sent.
    if (not previous_password or
            not temp_password or
            not temp_password_verify):
        flash(
            "You need to input your passwords. Try again.",
            'danger'
        )

        # Allow the user to retry the form if password not supplied.
        return render_template(
            "user/change_password_form.html",
            form=form,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Check password lengths are within acceptable lengths.
    if (len(str(previous_password)) < 5 or
            len(str(temp_password)) < 5 or
            len(str(temp_password_verify)) < 5 or
            len(str(previous_password)) > 70 or
            len(str(temp_password)) > 70 or
            len(str(temp_password_verify)) > 70):
        flash(
            "Passwords must be between 5 and 70 characters",
            'danger'
        )

        # Allow the user to retry the form if passwords are not valid length.
        return render_template(
            "user/change_password_form.html",
            form=form,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Check new passwords are equal
    if str(temp_password) != str(temp_password_verify):
        flash(
            "New Passwords are not the same. Please check your input.",
            'danger'
        )

        # Allow the user to retry the form if passwords are not equal.
        return render_template(
            "user/change_password_form.html",
            form=form,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Check that Previous and Current Passwords are not equal
    if (str(previous_password) == str(temp_password_verify) or
            str(previous_password) == str(temp_password)):

        flash(
            "Previous Password and new Password are the same. Please check "
            "your input.",
            'danger'
        )

        # Allow the user to retry the form if passwords are not equal.
        return render_template(
            "user/change_password_form.html",
            form=form,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # All checks passed

    # Set User ID from session here for convenience
    temp_user_id = session.get('user_id', False)

    # Check that User ID has not gone away
    # Validate if User ID in session is existent.
    if (not temp_user_id or
            not db.session.query(exists().where(
            User.id == str(temp_user_id))).scalar()):

        # Clear session state by logging them out.
        logout()

        flash(
            'We could not find your User ID so we logged you out. Please '
            'try logging in again and then retry the process.',
            'danger'
        )

        # Redirect the user back to the home page.
        return redirect(url_for('general.home'))

    # Select the user, then reset the password.
    existing_user = (
        db.session.query(User)
        .filter(User.id == str(temp_user_id))
        .first()
    )

    # Check if previously input password validates first.
    # log method used.
    if not existing_user.authenticate(str(previous_password)):
        flash(
            "Previous password must match the current password before "
            "changing to a new password. This has been logged.",
            'danger'
        )

        # Allow the user to input a different password.
        return render_template(
            "user/change_password_form.html",
            form=form,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Check if newly input password validates first before needing to commit.
    # no log method used
    if existing_user.authenticate_no_log(str(temp_password)):
        flash(
            "New Password must not be the same as the existing password.",
            'danger'
        )

        # Allow the user to input a different password if they supplied the
        # same password that was stored.
        return render_template(
            "user/change_password_form.html",
            form=form,
            recaptcha_v2_client=google_recaptcha_v2_key
        )

    # Set new Password
    existing_user.encrypted_password = str(temp_password)

    # Encrypt password
    existing_user.encrypt_password()

    # Finally, commit to database and set session objects.
    db.session.commit()

    flash(
        "New Password has been successfully set!",
        'success'
    )

    # Redirect back to home page
    return redirect(url_for('general.home'))


@user_bp.route(
    "/user_delete"
)
def user_delete():
    """
    This route is used to log a user out, and delete, removing all information
    from the database.

    This deletes their data.
    """

    # Check if User is not logged in.
    if not session.get('user_id', False):
        flash(
            "Sorry, you cannot access this page since you are not logged in.",
            'danger'
        )

        # Send user back to homepage
        return redirect(url_for('general.home'))

    # Check if email is set in the email session.
    if not session.get('email', False):
        flash(
            "You're not authenticated using Email.",
            'danger'
        )

        # Send user back to homepage
        return redirect(url_for('general.home'))

    # Database operations

    temp_id = session.get('user_id', False)

    # Check that User exists
    if (not temp_id or
            not (db.session.query(exists().where(
                User.id == temp_id)).scalar())):
        flash(
            "There was an error, we could not locate you in our Database",
            'danger'
        )

        # Clear Session
        clear_email_session()

        # Send user back to homepage
        return redirect(url_for('general.home'))

    # Select the User.
    existing_user = (
        db.session.query(User)
        .filter(User.id == temp_id)
        .first()
    )

    # Delete the found User.
    db.session.delete(existing_user)

    # Commit
    db.session.commit()

    # Clear Session
    clear_email_session()

    flash(
        "Your email and user account has been deleted and any associated "
        "details has been removed from our systems.",
        'success'
    )

    # Send user back to homepage
    return redirect(url_for('general.home'))


@user_bp.route(
    "/logout"
)
def logout():
    """
    This route is used to remove session data from the user.

    This does not delete their data, only removes their session so that they
    can switch accounts.
    """

    # Check if user is not logged in.

    if session.get('user_id', False):
        session.pop('user_id', None)

    else:
        flash(
            "Sorry, you cannot access this page since you have not "
            "logged in.",
            'danger'
        )

        # Send the user back to homepage.
        return redirect(url_for('general.home'))

    if session.get('profile_id', False):
        session.pop('profile_id', None)

    if session.get('username', False):
        session.pop('username', None)

    if session.get('email', False):
        session.pop('email', None)

    if session.get('email_state', False):
        session.pop('email_state', None)

    if session.get('username_state', False):
        session.pop('username_state', None)

    if session.get('email_registration', False):
        session.pop('email_registration', None)

    # GitHub Session objects

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

    # Google Session objects

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

    flash(
        "You have logged out successfully.",
        'success'
    )

    return redirect(url_for('general.home'))


# DEBUG FUNCTION
@user_bp.route(
    "/check_all_session_objects"
)
def check_all_session_objects():
    """
    Debug function
    Outputs all possible session objects and outputs to the user.

    This shows tokens provided by SSO logins so disable during production.
    """

    if not session.get('user_id', False):

        flash(
            "Sorry, you cannot access this page since you have not "
            "logged in.",
            'danger'
        )

        # Send the user back to the homepage.
        return redirect(url_for('general.home'))

    return_string = ""

    """
    General Session
    """

    if session.get('user_id', False):
        return_string += "User ID: "
        return_string += str(session.get('user_id', None)) + "<br/>"

    """
    Email Session
    """

    if session.get('username', False):
        return_string += "Username: "
        return_string += str(session.get('username', None)) + "<br/>"

    if session.get('email', False):
        return_string += "Email: "
        return_string += str(session.get('email', None)) + "<br/>"

    if session.get('email_state', False):
        return_string += "Email State: "
        return_string += str(session.get('email_state', None)) + "<br/>"

    if session.get('username_state', False):
        return_string += "Username State: "
        return_string += str(session.get('username_state', None)) + "<br/>"

    if session.get('email_registration', False):
        return_string += "Email Registration: "
        return_string += str(session.get('email_registration', None)) + "<br/>"

    """
    GitHub Session
    """

    if session.get('sso_github_token', False):
        return_string += "Github SSO Token: "
        return_string += str(session.get('sso_github_token', None)) + "<br/>"

    if session.get('sso_github', False):
        return_string += "Github SSO: "
        return_string += str(session.get('sso_github', None)) + "<br/>"

    if session.get('sso_github_id', False):
        return_string += "Github SSO ID: "
        return_string += str(session.get('sso_github_id', None)) + "<br/>"

    if session.get('sso_github_email', False):
        return_string += "Github SSO Email: "
        return_string += str(session.get('sso_github_email', None)) + "<br/>"

    if session.get('sso_github_name', False):
        return_string += "Github SSO Name: "
        return_string += str(session.get('sso_github_name', None)) + "<br/>"

    if session.get('sso_github_image', False):
        return_string += "Github SSO Image: "
        return_string += str(session.get('sso_github_image', None)) + "<br/>"

    """
    Google Session objects
    """

    if session.get('sso_google_token', False):
        return_string += "Google SSO: "
        return_string += str(session.get('sso_google_token', None)) + "<br/>"

    if session.get('sso_google', False):
        return_string += "Google SSO: "
        return_string += str(session.get('sso_google', None)) + "<br/>"

    if session.get('sso_google_id', False):
        return_string += "Google SSO ID: "
        return_string += str(session.get('sso_google_id', None)) + "<br/>"

    if session.get('sso_google_name', False):
        return_string += "Google SSO Name: "
        return_string += str(session.get('sso_google_name', None)) + "<br/>"

    if session.get('sso_google_email', False):
        return_string += "Google SSO Email: "
        return_string += str(session.get('sso_google_email', None)) + "<br/>"

    if session.get('sso_google_image', False):
        return_string += "Google SSO Image: "
        return_string += str(session.get('sso_google_image', None)) + "<br/>"

    return return_string
