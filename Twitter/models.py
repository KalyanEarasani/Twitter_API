from app import db

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(280))
    created_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Tweet {self.id}>'
    
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    twitter_id = db.Column(db.Integer, unique=True)
    access_token = db.Column(db.String(200))
    access_token_secret = db.Column(db.String(200))
    last_sync = db.Column(db.DateTime)

    tweets = db.relationship('Tweet', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.name}>'
