from flask_wtf import FlaskForm
from wtforms import validators, EmailField, SubmitField


class SingleEmailForm(FlaskForm):
    """
    Form to request a single input (Email) from a user.

    Email (6-128 Length) [Prefilled]
    """

    """Must be filled"""
    email = EmailField("E-Mail", [
        validators.Length(6, 128),
        validators.InputRequired(message='Email cannot be empty'),
        ],
                     render_kw={
                         'placeholder': 'Email Address',
                         'autocomplete': "email"
                     })

    submit = SubmitField(render_kw={
        'class': "btn btn-primary bg-primary text-light py-4 px-5 h6 "
                 "placeholder-wave"
    })
