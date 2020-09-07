from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, PasswordField, TextAreaField, validators 
from wtforms.validators import DataRequired, Length, NumberRange, InputRequired

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

class LoginForm(FlaskForm):
    contact = StringField('Contact', validators=[DataRequired(), Length(min=10, max=10)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Send OTP')

class OtpForm(FlaskForm):
    otp = StringField('Contact', validators=[DataRequired()])
    submit = SubmitField('Login')