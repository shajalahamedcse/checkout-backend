# manage.py

import os
import unittest

from flask_script import Manager, Server, Command, Option
from flask_migrate import Migrate, MigrateCommand
from src.server import app, db, models


migrate = Migrate(app, db)
manager = Manager(app)
# server manager
manager.add_command("runserver", Server(host='0.0.0.0', port='8000'))

# migrations
manager.add_command('db', MigrateCommand)


@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all()


@manager.command
def drop_db():
    """Drops the db tables."""
    db.drop_all()



if __name__ == '__main__':
    manager.run()
