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
        return f"<User id={u.id} first_name={u.first_name} last_name={u.last_name} image_url= {u.image_url}>"
    
    @classmethod
    def full_name(self):
        """Return full name of user"""
        return f'{self.first_name} {self.last_name}'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    first_name = db.Column(db.Text,
                           nullable=False,
                           unique=False)
    
    last_name = db.Column(db.Text,
                          nullable=False,
                          unique=False)
    
    image_url = db.Column(db.Text,
                          nullable=False
                          ) 