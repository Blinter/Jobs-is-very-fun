from flask_wtf import FlaskForm
from wtforms import validators, SubmitField, PasswordField


class ChangePassword(FlaskForm):
    """
    Form for resetting a Password for a currently logged-in user.
    link.

    Previous Password (5-70 Length)
    Password (5-70 Length)
    Password Verification (5-70 Length)
    """

    """Must be filled"""
    password_previous = PasswordField("Current Password", [
        validators.Length(5, 70),
        validators.InputRequired(message='Password cannot be empty'),
        ],
                     render_kw={
                         'placeholder': 'Password (Between 5-70 Characters)',
                         'autocomplete': "password"
                     })

    password = PasswordField("New Password", [
        validators.Length(5, 70),
        validators.InputRequired(message='Password cannot be empty'),
        ],
                     render_kw={
                         'placeholder': 'Password (Between 5-70 Characters)',
                         'autocomplete': "password"
                     })

    password_verify = PasswordField("New Password (Again)", [
        validators.Length(5, 70),
        validators.InputRequired(message='Password cannot be empty'),
        ],
                     render_kw={
                         'placeholder': 'Password (Between 5-70 Characters)',
                         'autocomplete': "password"
                     })

    submit = SubmitField("Reset", render_kw={
        'class': "btn btn-primary bg-success text-white py-4 px-5 h6 "
                 "placeholder-wave"
    })
