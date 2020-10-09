import os
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from logging.config import dictConfig


app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
CORS(app)

app_settings = os.getenv(
    'APP_SETTINGS',
    'src.server.config.DevelopmentConfig'
)

app.config.from_object(app_settings)
db = SQLAlchemy(app)

from src.server.home.views import home_blueprint

app.register_blueprint(home_blueprint)