from app import create_app
from app import db,User,Task
from flask_script import Manager

from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

config_class = config['development']

app = create_app(config_class)

migrate = Migrate(app, db)

if __name__ == "__main__":
    manager = Manager(app)

    manager.add_command("db", MigrateCommand)
    manager.run()