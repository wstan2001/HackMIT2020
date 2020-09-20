from app import db


class Polls(db.Model):
    __tablename__ = 'polls'
    name = db.Column(db.String, primary_key=True)
    latest = db.Column(db.Integer)
    timestamp = db.Column(db.String)

    def __init__(self, name, latest, timestamp):
        self.name = name
        self.latest = latest
        self.timestamp = timestamp