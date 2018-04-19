from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required
from ..email import mail_message
from ..models import Subscribe,Post
from .forms import Subscribe_form,Post_form
from .. import db
from flask import flash
# Views
@main.route('/',methods = ["GET","POST"])
def index():

    form = Subscribe_form()

    if form.validate_on_submit():
        subscriber=Subscribe(email =form.email.data,username=form.username.data)
        db.session.add(subscriber)
        db.session.commit()
        mail_message("Welcome to the trendy T's blog","email/welcome_user",subscriber.email,subscriber=subscriber)

        flash("Welcome new subscriber")
        return redirect(url_for('main.index'))
    return render_template('index.html',subscribe_form = form )

@main.route('/writers')
@login_required
def writers():
    form =Post_form()
    if form.validate_on_submit():
        post=form.post.data
        title=form.title.data
        new_post =Post(post_id=post.id,username=username,post_title=title,post_date=post.date)
        new_post.save_post()
        flash("succefully published")
        return redirect(url_for('main.index') 

    return render_template('write.html',title=title)
