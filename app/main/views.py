from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required,current_user
from ..email import mail_message
from ..models import Subscribe,Post,Comments
from .forms import Subscribe_form,Post_form,Comments_form
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
    posts=Post.query.all()

    return render_template('index.html',subscribe_form = form,posts=posts)

@main.route('/writers',methods=["GET","POST"])
@login_required

def writers():
    form =Post_form()

    if form.validate_on_submit():
        posts=Post(username=form.username.data,post_title=form.post_title.data,post=form.post.data)
        db.session.add(posts)
        db.session.commit()
        flash("succefully published")
        return redirect(url_for('main.index'))

    return render_template('write.html',post_form=form)
@main.route('/blogs/<int:id>',methods=["GET","POST"])
def blogs(id):
    form=Comments_form()

    if form.validate_on_submit():
        comments=Comments(username=form.username.data,comment=form.comment.data)
        db.session.add(comments)
        db.session.commit()
        flash("comment added")
        return redirect(url_for('main.index'))

    posts=Post.query.filter_by(id=id).first()
    comment=Comments.query.filter_by(id=id)

    return render_template("blogs/blog.html",posts=posts,comments_form=form,comment=comment)
