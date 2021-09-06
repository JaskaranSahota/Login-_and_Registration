from flask_app.models.login import Login
from flask import render_template,redirect,request,session
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt 
from flask_app.models.registration import Registartion
bcrypt = Bcrypt(app)  
@app.route('/login',methods=["POST","GET"])
def final():
    if request.method=="GET":
        return render_template("login.html")
    else:
        data = { "email" : request.form["email"] }
        print(data)
        user_in_db = Registartion.get_all(data)
        # user is not registered in the db
        if not user_in_db:
            flash("No account")
            return redirect("/")
        if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
            # if we get False after checking the password
            flash("Invalid Email/Password")
            return redirect('/')
        # if the passwords matched, we set the user_id into session
        session['user_id'] = user_in_db.id
        # never render on a post!!!
    return redirect('/success')
@app.route('/success')
def success():
    if 'user_id' in session:
        data={
            'id':session['user_id']
        }
        return render_template("success.html",user=Registartion.get_one(data))
    else:
        return redirect('/logout')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
