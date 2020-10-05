from flask import Flask
#from application import routes

app = Flask(__name__)

from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
import os

file_path = os.path.abspath(os.getcwd())+"\database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)

login_manager.login_view = "users.login"
login_manager.login_message = u"You need to login to access this link."

from application import routes, models, forms, otp
