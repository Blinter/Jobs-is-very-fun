from flask_wtf import FlaskForm
from wtforms import validators, StringField, SubmitField, PasswordField


class LoginEmailOrPassword(FlaskForm):
    """Form for logging in a user using an email or password.

    Email or Username (3-128 Length)
        Username (3-20 Length) or Email (6-128 Length)
    Password (5-70 Length)
    """

    """Must be filled"""
    email_or_username = StringField("Email or Username", [
        validators.Length(3, 128),
        validators.InputRequired(message='Email cannot be empty'),
        ],
                     render_kw={
                         'placeholder': 'Email or Username',
                         'autocomplete': "username",
                     })

    password = PasswordField("Password", [
        validators.Length(5, 70),
        validators.InputRequired(message='Password cannot be empty'),
        ],
                     render_kw={
                         'placeholder': 'Password (Between 5-70 Characters)',
                         'autocomplete': "password"
                     })

    submit = SubmitField("Login", render_kw={
        'class': "btn btn-primary bg-success text-white py-4 px-5 h6 "
                 "placeholder-wave"
    })
