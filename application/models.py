from application import app, db, login_manager
from flask_login import UserMixin

x = 10

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, nullable=False, default=x+1)
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
    category = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    employer_contact = db.Column(db.String(10), db.ForeignKey('user.contact'), nullable=False)

    def __repr__(self):
        return f"JobPost('{self.title}', '{self.category}', '{self.employer_contact}', '{self.email}','{self.location}')"
