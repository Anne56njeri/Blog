from  flask_wtf import FlaskForm
from ..models import Subscribe
from wtforms import ValidationError
from  wtforms.validators import Required,Email
from wtforms import StringField,PasswordField,SubmitField,BooleanField,DateTimeField,TextAreaField


class Subscribe_form(FlaskForm):
    username = StringField('Enter your first name',validators=[Required()])
    email=StringField('Enter your email to recieve alerts ',validators=[Required(),Email()])
    submit =SubmitField('Subscribe..')
    def validate_email(self,data_field):
        if Subscribe.query.filter_by(email=data_field.data).first():
            raise ValidationError(' that email is already taken')
    def validate_name(self,data_field):
        if Subscribe.query.filter_by(username = data_field.data).first():
            raise ValidationError('that user name is already taken')
class Postform(FlaskForm):
    username=StringField('Enter your username writer...',validators=[Required()])
    post_title=StringField('Enter the title of the post',validators=[Required()])
    date =DateTimeField('Enter the date',format='%m%d%y')
    post =TextAreaField('Enter your post'validators=[Required()])
    Submit=SubmitField('Submit Post')
