from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

with open('/etc/config.json') as config_file:
	config = json.load(config_file)

app = Flask(__name__)
app.config['SECRET_KEY'] = config.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///facilities.db"
db = SQLAlchemy(app)

from website import routes
