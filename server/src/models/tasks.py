from src import db
from datetime import datetime

class Task(db.Model):
    __tablename__='tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(255)) # Optional
    deadline = db.Column(db.DateTime) # Optional
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    