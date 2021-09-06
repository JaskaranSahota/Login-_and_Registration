from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX =re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Login:
    def __init__(self,data) -> None:
        self.id=data['id'],
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    @staticmethod
    def valid(user):
        is_valid=True
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email","login")
            is_valid=False
        if len(user['password'])<5:
            flash("Weak Password","login")
            is_valid=False
        return is_valid

        