from flask_wtf import FlaskForm
from application.models import User
from wtforms import StringField, SubmitField, SelectField, BooleanField, PasswordField, TextAreaField, validators 
from wtforms.validators import DataRequired, Length, NumberRange, InputRequired, ValidationError, Email

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    contact = StringField('Contact', validators=[DataRequired(), Length(min=10, max=10)])
    location = StringField('Location', validators=[DataRequired(), Length(min=2, max=250)])

    categorychoices = ['Electronics', 'IT', 'Waterworks', 'Housekeeping', 'Beautician', 'Construction', 'Teaching', 'Furnishing']
    educationchoices = ['Primary', 'Secondary', 'Sr. secondary', 'Graduate', 'P. Graduate', 'Diploma', 'Doctorate']
    
    category = SelectField('Category', choices = categorychoices, default=1, validators=[DataRequired()])
    education = SelectField('Education', choices= educationchoices, default=1, validators=[DataRequired()])
    
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_contact(self, contact):
        user = User.query.filter_by(contact=contact.data).first()
        if user:
            raise ValidationError('This phone number is already registered.')

class LoginForm(FlaskForm):
    contact = StringField('Contact', validators=[DataRequired(), Length(min=10, max=10)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Send OTP')

class OtpForm(FlaskForm):
    otp = StringField('Enter OTP', validators=[DataRequired()])
    submit = SubmitField('Login')

class NewPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=20)])
    categorychoices = ['Electronics', 'IT', 'Waterworks', 'Housekeeping', 'Beautician', 'Construction', 'Teaching', 'Furnishing']
    category = SelectField('Category', choices = categorychoices, default=1, validators=[DataRequired()])
    email = StringField('Email')
    location = StringField('Location', validators=[DataRequired(), Length(min=2, max=250)])
    submit = SubmitField('Post')
