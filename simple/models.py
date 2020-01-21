from . import db,login_manager
from flask_login import UserMixin

#the database schema

class User(db.Model,UserMixin):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(25),nullable=False)
    email=db.Column(db.String(80),nullable=False,unique=True)
    gender=db.Column(db.String(10),nullable=False)
    location=db.Column(db.String(20),nullable=False)
    password=db.Column(db.Text(),nullable=False)
    

    def __repr__(self):
        return "{}".format(self.name)


class Post(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    title=db.Column(db.String(20),nullable=False)
    content=db.Column(db.Text(),nullable=False)

    def __repr__(self):
        return "{}".format(self.title)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))