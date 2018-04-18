from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required
from ..email import mail_message
from ..models import Subscribe
from .forms import Subscribe_form
from .. import db
from flask import flash
# Views
@main.route('/')
def index():
	title = 'Welcome to the personal blog app'
    form = Subscribe_form
    if form.validate_on_submit():
        subscriber=Subscribe(email =form.email.data,username=form.username.data)
        db.session.add(subscriber)
        db.session.commit()
        mail_message("Welcome to the trendy T's blog","email/welcome_sub",subscriber.email,subscriber=subscriber)

        return flash("Welcome new subscriber")


    return render_template('index.html',title = title)
@main.route('/writers')
@login_required
def writers():
    title = 'Welcome writer'
    return render_template('write.html',title=title)
