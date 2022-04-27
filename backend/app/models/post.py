from .db import db

class Post(db.Document):
    title = db.StringField(required=True, max_length=50)
    count = db.IntField(required=True)
    url = db.URLField()
