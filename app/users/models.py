from app.database import db
import bcrypt

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    lastname = db.Column(db.String)
    mail = db.Column(db.String)
    password = db.Column(db.String)
    city = db.Column(db.String)
    salt = db.Column(db.String)
    enabled = db.Column(db.Boolean, nullable=True)
    image = db.Column(db.LargeBinary, nullable=True)
    image_mime = db.Column(db.String, nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=True)

    def __init__(self, **kwargs):
        super(User, self).__init__(self, kwargs)
        self.enabled = True
        self.salt = bcrypt.gensalt()

    def set_image(self, file):
        pass

    def __eq__(self, other: 'User') -> bool:
        return (other.mail == self.mail) and (self.password == other.password)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    role = db.Column(db.String)
    users = db.relationship('User', backref='role')
