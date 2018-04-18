from  flask_wtf import FlaskForm
from ..models import Subscribe
from wtforms import ValidationError
from  wtforms.validators import Required,Email
from wtforms import StringField,PasswordField,SubmitField,BooleanField


class Subscribe_form(FlaskForm):
    name = StringField('Enter your first name',validators=[Required()])
    email=StringField('Enter your email to recieve alerts ',validators=[Required(),Email()])
