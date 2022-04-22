from db import db

class PostModel(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
