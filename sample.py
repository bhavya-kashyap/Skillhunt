from application.routes import db, User, JobPost

db.create_all()

user1 = User(id = "1", name="bhavya", contact="8949870585", location="jaipur", category="IT", education="Graduate", description="hello")
user2 = User(id = "2", name="kashyap", contact="9024666793", location="jaipur", category="IT", education="Graduate", description="hello")

db.session.add(user1)
db.session.add(user2)

db.session.commit()

#User.query.filter_by(name='bhavya').all()
#user = User.query.filter_by(contact='8949870585').first()
#user.name
#user.jobs
# for job in user.jobs:
#        print(job.title)