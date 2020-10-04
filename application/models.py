from application import app
from flask_sqlalchemy import SQLAlchemy
import os

file_path = os.path.abspath(os.getcwd())+"\database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    name = db.Column(db.String(50), nullable=False)
    contact = db.Column(db.String(10), primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    education = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1500), nullable=False)
    jobs = db.relationship('JobPost', backref='employer', lazy=True)

    def __repr__(self):
        return f"User('{self.name}', '{self.contact}')"

class JobPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    employer_contact = db.Column(db.String(10), db.ForeignKey('user.contact'), nullable=False)

    def __repr__(self):
        return f"JobPost('{self.title}', '{self.contact}', '{self.email}','{self.location}')"
