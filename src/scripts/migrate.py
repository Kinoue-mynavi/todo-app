from flask_script import Command
from src import db
from src.models.tasks import Task

class InitDB(Command):
    "create datbase"
    
    def run(self):
        db.create_all()