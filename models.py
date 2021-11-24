from enum import unique
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    
    """Models for Blogly."""


class User(db.Model):
    
    __tablename__ = 'users'

    def __repr__(self):
        u = self
        return f"<User id={u.id} name={u.name} hunger = {u.hunger}>"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    first_name = db.Column(db.String,
                           nullable=False,
                           unique=False)
    
    last_name = db.Column(db.String,
                          nullable=False,
                          unique=False)
    
    image_url = db.Column(db.String,
                          nullable=True,
                          ) 