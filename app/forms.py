from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, FloatField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class UserLocationsForm(FlaskForm):
    location1_coords = StringField("Location 1 Coordinates", validators=[DataRequired()])
    location2_coords = StringField("Location 2 Coordinates", validators=[DataRequired()])
    
    submit = SubmitField("Submit")
