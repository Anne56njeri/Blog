from flask import render_template,redirect,url_for
from . import auth
from ..models import Writer
from .forms import Registration
from .. import db

@auth.route('/login')
def login():
    return render_template('auth/login.html')
@auth.route('/register',methods = ["GET","POST"])
def register_writer():
    form =Registration()
    if form.validate_on_submit():
        writer=Writer(email=form.email.data,username=form.username.data,password=form.password.data)
        db.session.add(writer)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title="New Account"
    return render_template('auth/register.html',registration=form )
