from app import db
from flask_sqlalchemy import column_property
from flask_login import UserMixin

# Define a base model for other database tables to inherit
class base_auth(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

class user_model(UserMixin, base_auth):    
    username = db.Column(db.String(100), unique=True)
    
    email           = db.Column(db.String(100), unique=True)
    password_hash   = db.Column(db.String(128))
    
    first_name      = db.Column(db.String(50))
    last_name       = db.Column(db.String(50))
    fullname        = column_property(firstname + " " + lastname)

    # Personal address
    address         = db.Column(db.String(50), nullable=True)
    city            = db.Column(db.String(50), nullable=True)
    country         = db.Column(db.String(50), nullable=True)
    postal_code     = db.Column(db.String(50), nullable=True)

    # Groups
    workgroup       = db.Column(db.String(50), nullable=True)
    company         = db.Column(db.String(50), nullable=True)

    # Authorisation Data: role & status
    role            = db.Column(db.SmallInteger, nullable=False)

    # statuses:
    # 0 - inactivated
    # 1 - activated
    # 2 - blocked
    status   = db.Column(db.SmallInteger, nullable=False)

    def __repr__(self):
        return '<User %r>' % (self.fullname) 