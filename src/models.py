from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return '<Person %r>' % self.username

#     def serialize(self):
#         return {
#             "username": self.username,
#             "email": self.email
#         }

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    zip = db.Column(db.Integer(20), nullable=False)
    

     def __repr__(self):
         return '<Users %r>' % self.firstname

     def serialize(self):
         return {
             "firstname": self.firstname,
             "lastname": self.lastname
             "email": self.email,
             "password": self.password,
             "zip": self.zip
         }

class Objects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    objectname = db.Column(db.String, nullable=False)
    recycle = db.Column(db.String, nullable=False)
    reuse = db.Column(db.String, nullable=False)
    reduce = db.Column(db.String, nullable=False)

    def __repr__(self):
         return '<Objects %r>' % self.objectname

     def serialize(self):
         return {
             "id": self.id,
             "objectname": self.objectname
             "recycle": self.recycle,
             "reuse": self.reuse,
             "reduce": self.reduce
         }
    
class ResourceCenters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    centername = db.Column(db.String, nullable=False)
    address = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    zip = db.Column(db.Integer, nullable=False)
    hours = db.Column(db.Integer, nullable=False)
    phonenumber = db.Column(db.integer, nullable=False)
    website = db.Column(db.String, nullable=True)
    type = db.Column(db.String, nullable=False)

    def __repr__(self):
         return '<ResourceCenters %r>' % self.firstname

     def serialize(self):
         return {
             "cetername": self.centername,
             "address": self.address,
             "city": self.city,
             "state": self.state,
             "zip": self.zip,
             "hours": self.hours,
             "phonenumber" self.phonenumber,
             "website": self.website,
             "type": self.type
         }

