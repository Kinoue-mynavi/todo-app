from flask_script import Manager
from src import app
from src.scripts.migrate import InitDB

if __name__ == "__main__":
    manager=Manager(app)
    manager.add_command("init_db", InitDB)
    manager.run()