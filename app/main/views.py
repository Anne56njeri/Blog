from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required

# Views
@main.route('/')
def index():
	title = 'Welcome to the personal blog app'
	return render_template('index.html',title = title)
