from email_validator import validate_email
import mysql.connector as sqltor
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helper_module import login_required,apology
from datetime import datetime
import math

all_states = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh",
              "Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka",
              "Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha",
              "Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand",
              "West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu",
              "Lakshadweep","National Capital Territory of Delhi","Puducherry"]

all_gender = ["M","F","O"]

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#Configure mysql database
mycon = sqltor.connect(host="localhost",user="root",password="1234",database="insurance")

db = mycon.cursor(prepared=True)

if mycon.is_connected:
    print("Connection Established")
else:
    raise "Connection Failed"

#Checks to see is user is active via javascript and displays different UI elements based on that
#wont be needed where @login_required
def render_session(name):
    if len(session) == 0:
        return render_template(name,session="absent")
    else:
        return render_template(name,session="present")

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_session("home.html")
    
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        
        email = request.form.get("email")
        if not email:
            return apology("Email not entered")
        if not validate_email(email):
            return apology("Please enter a valid email")
        
        password = request.form.get("password")
        if not password:
            return apology("must provide password")
        
        db.execute("SELECT password,id FROM user WHERE email = ?", (email,))
        login_email = db.fetchall()
        print(login_email)
        if len(login_email) != 1 or not check_password_hash(login_email[0][0], password):
            return apology("invalid username and/or password")
        
        session["user_id"] = login_email[0][1]
        return redirect("/")
    else:
        return render_session("login.html")
    
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        if not email:
            return apology("Email not filled")
        if not validate_email(email):
            return apology("Please enter a valid email")
        db.execute("SELECT email FROM user WHERE email = ?", (email,))
        temp = db.fetchall()
        if len(temp) != 0:
            return apology("Email you entered is already in our database. Maybe try logging in ?")
        password = request.form.get("password")
        if not password:
            return apology("Password not filled")
        if len(password) < 10:
            return apology("Password was less than 1o characters")
        if not password.isalnum():
            return apology("Password was not alphanumeric")
        confirmation = request.form.get("confirmation")
        if password != confirmation:
            return apology("Password and Confirmation Password do not match")       
        name = request.form.get("name")
        if not name:
            return apology("Name not filled")
        temp = int(request.form.get("gender"))
        if temp == 0:
            return apology("Gender not entered")
        gender = all_gender[int(temp) - 1]
        dob = request.form.get("dob")
        if not dob:
            return apology("Date of birth not filled not filled")
        phone = request.form.get("phone")
        if not phone:
            return apology("Phone number not filled")  
        city = request.form.get("city")
        if not city:
            return apology("City not filled")
        temp = request.form.get("state")
        if temp == 0:
            return apology("State not entered")
        state = all_states[int(temp) - 1]
        address = request.form.get("address")
        if not address:
            return apology("Address not filled")
        print(email,password,confirmation,name,gender,dob,phone,city,state,address)
        db.execute("INSERT INTO user (name,gender,phone,address,email,password,state,city,dob) VALUES (?,?,?,?,?,?,?,?,?);", (name,gender,phone,address,email,generate_password_hash(password),state,city,dob))
        mycon.commit()
        return redirect("/")
    else:
        length = len(all_states)
        return render_template("register.html",states=all_states,len_states=length)
    
@app.route("/getprice", methods=["GET", "POST"])
@login_required
def getprice():
    if request.method == "POST":

        #Code

        return redirect("/")
    else:
        db.execute("SELECT dob,state,gender FROM user WHERE id = ?",(session["user_id"],))
        data = db.fetchall()
        year = data[0][0].split("/")[2]
        state = data[0][1]
        gender = data[0][2]
        if gender == "M":
            gender = "male"
        elif gender == "F":
            gender = "female"
        else:
            return apology("Services for 'Other' gender is not yet available")
        statement = "SELECT " + gender + " FROM lifeexpt WHERE year = ?"
        db.execute(statement,(year,))
        exp = db.fetchall()[0][0]
        cur_year = datetime.now().year
        age_left = exp - cur_year + int(year)
        payment_years = math.floor(age_left - 1)
        print(payment_years)
        
        return render_template("price.html",session="present")