from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class Writer(UserMixin,db.Model):
    __tablename__='writers'
    id =db.Column(db.Integer,primary_key =True)
    username =db.Column(db.String(255))
    email=db.Column(db.String(255),unique =True,index=True)
    pass_secure=db.Column(db.String(255))
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self,password):
        self.pass_secure=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    def __repr__(self):
        return f'User {self.username}'
    '''
    this retrieves a user when a unique identifier is passed in this cause we pass in the id
    '''
    @login_manager.user_loader
    def load_user(user_id):
        return Writer.query.get(int(user_id))
class Subscribe(db.Model):
    __tablename__='subscribe'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(255),unique=True,index=True)
    def __repr__(self):
        return f'User {self.username}'
class Post(db.Model):
    __tablename__='posts'
    id=db.Column(db.Integer,primary_key =True)
    post_id=db.Column(db.Integer)
    username=db.Column(db.Integer,primary_key =True)
    post_title=db.Column(db.String(255))
    post_date=db.Column(db.DateTime,default=datetime.utcnow)

    def save_post(self):
        db.session.add(self)
        db.session.commit()
    def get_post(self):
        posts = Post.query.filter_by(post_id=id).all()
        return posts
    
