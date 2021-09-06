from flask import render_template,redirect,request,session
from flask_app import app
from flask_bcrypt import Bcrypt   
from flask_app.models.registration import Registartion     
bcrypt = Bcrypt(app)   
@app.route('/')
def home():
    return render_template("Registration.html")

@app.route('/register',methods=["POST","GET"])
def register():
    if request.method=="GET":
        return render_template("Registration.html")
    else:
        if Registartion.valid(request.form):
            pw_hash = bcrypt.generate_password_hash(request.form['password'])
            print(pw_hash)
            data= {
                "first_name":request.form['first_name'],
                'last_name':request.form['last_name'],
                'email':request.form['email'],
                'password':pw_hash,
                'password2':pw_hash
            }
            user_id=Registartion.save(data)
            session['user_id']=user_id
            return redirect('/success')
        else:
            return redirect('/register')
    
