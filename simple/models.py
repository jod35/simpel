from . import db

#the database schema

class User(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(25),nullable=False)
    email=db.Column(db.String(80),nullable=False)
    gender=db.Column(db.String(10),nullable=False)
    location=db.Column(db.String(20),nullable=False)
    password=db.Column(db.Text(),nullable=False)

    def __repr__(self):
        return "{}".format(self.name)

