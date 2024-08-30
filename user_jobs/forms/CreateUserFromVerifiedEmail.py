from flask_wtf import FlaskForm
from wtforms import validators, StringField, SubmitField, PasswordField


class CreateUserFromVerifiedEmail(FlaskForm):
    """Form for registering an EMail Address.

    Email (6-128 Length) [Prefilled]
    Username (3-20 Length) [Prefilled]
    Password (5-70 Length)
    """

    """Must be filled"""
    email = StringField("E-Mail (Verified)", [
        validators.Length(6, 128),
        validators.InputRequired(message='Email cannot be empty'),
        ],
                     render_kw={
                         'class': 'form-control py-3 text-black-50 bg-info '
                                  'mt-2 h5 disabledTextInput',
                         'placeholder': 'Email Address',
                         'autocomplete': "email",
                         'readonly': True,
                     })

    username = StringField("Username", [
        validators.Length(3, 20),
        validators.InputRequired(message='Username cannot be empty'),
        ],
                     render_kw={
                         'placeholder': 'Username (Between 3-20 Characters)',
                         'autocomplete': "username"
                     })

    password = PasswordField("Password", [
        validators.Length(5, 70),
        validators.InputRequired(message='Password cannot be empty'),
        ],
                     render_kw={
                         'placeholder': 'Password (Between 5-70 Characters)',
                         'autocomplete': "password"
                     })

    submit = SubmitField("Register", render_kw={
        'class': "btn btn-primary bg-success text-white py-4 px-5 h6 "
                 "placeholder-wave"
    })
