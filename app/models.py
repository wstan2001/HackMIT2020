from app import db


class Polls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    latest = db.Column(db.Integer)
    timestamp = db.Column(db.String)