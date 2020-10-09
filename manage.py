# manage.py

import os
import unittest

from flask_script import Manager, Server, Command, Option
from flask_migrate import Migrate, MigrateCommand
from src.server import app

manager = Manager(app)
# server manager
manager.add_command("runserver", Server(host='0.0.0.0', port='8000'))


if __name__ == '__main__':
    manager.run()
