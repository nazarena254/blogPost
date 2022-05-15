from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from wtforms.validators import InputRequired, Email, EqualTo
from ..models import User

class SignUpForm(FlaskForm): #Signup form
    first_name = StringField("Your First Name", validators=[InputRequired()])
    last_name = StringField("Your Last Name", validators=[InputRequired()])
    username = StringField("Your Username", validators=[InputRequired()])
    email = StringField("Your Email Address", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired(), 
                             EqualTo("password_confirm", message = "Passwords must match")])
    password_confirm = PasswordField("Confirm Password", validators=[InputRequired()])
    submit = SubmitField("Sign Up")

    #Custom email validation
    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("There is an account with that email")

    #Custom username validation
    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError("That username is taken")

class LoginForm(FlaskForm): #login form
    email = StringField("Your Email Address", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Sign In")