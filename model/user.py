from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    branch_id = db.Column(db.Integer, nullable=False)  # just store ID, no FK
    username = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
