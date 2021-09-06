from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX =re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
# Create new class
class Registartion:
    db="login_and_regisration"
    def __init__(self,data) -> None:
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.password2=data['password2']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def save(cls,data):
        query="INSERT INTO registration(first_name,last_name,email,password,password2)VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s,%(password2)s);"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_all(cls,data):
        query="SELECT * FROM registration where email=%(email)s;"
        result=connectToMySQL(cls.db).query_db(query,data)
        print(result)
        if len(result)>0:
            return (cls(result[0]))
        else:
            return False

    @classmethod
    def get_one(cls,data):
        query="SELECT * FROM registration where id=%(id)s;"
        result=connectToMySQL(cls.db).query_db(query,data)
        return(cls(result[0]))

    @staticmethod
    def valid(user):
        query="SELECT * FROM registration where email=%(email)s;"
        result=connectToMySQL(Registartion.db).query_db(query,user)
        is_valid=True
        if  len(user['first_name'])<2 and not user["first_name"].isalpha():
            flash("First Name:Invalid Entry'not alphabets' or 'less than 2 characters'", "register")
            is_valid=False
        if  len(user['last_name'])<2 and not user["last_name"].isalpha():
            flash("Last Name:Invalid Entry'not alphabets' or 'less than 2 characters'", "register")
            is_valid=False
        if len(result)>0:
            flash("Email:Email already taken","register")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Email:Invalid email","register")
            is_valid=False
        if len(user['password'])<5:
            flash("Password:Weak Password","register")
            is_valid=False
        if user['password']!=user['password2']:
            flash("Password:Password does not match","register")
            is_valid=False
        return is_valid

        
        

    