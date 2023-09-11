import os
from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required



# Configure application
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
'''uri = os.getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://")
db = SQL(uri)''' #TO CONNECT TO ACTUAL DATABASE

db = SQL("sqlite:///links.db")

@app.after_request
def after_request(response):
    # Ensure responses aren't cached
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    links = db.execute("SELECT link,icon,name,node FROM links WHERE user_id = ?", session["user_id"])
    renodes = db.execute("SELECT id,name FROM renode WHERE user_id = ?", session["user_id"])
    return render_template("/links.html", links=links, renodes = renodes)

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":

        if not request.form.get("username"):
            return apology("must provide username", 403)

        elif not request.form.get("password"):
            return apology("must provide password", 403)

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username or not password or not confirmation:
            return apology("Username/Password not filled correctly")
        temp = db.execute("SELECT username FROM users WHERE username = ?", username)

        if len(temp) != 0:
            return apology("Username already exists")

        if password != confirmation:
            return apology("Passwords do not match")

        db.execute("INSERT INTO users (username,hash) VALUES (?,?)", username, generate_password_hash(password))

        return redirect("/")
    else:
        return render_template("/register.html")

@app.route("/changepass", methods=["GET", "POST"])
@login_required
def changepass():
    """change password"""
    if request.method == "POST":
        oldpass = (db.execute("SELECT hash FROM users WHERE id = ?", session["user_id"]))[0]["hash"]
        if not check_password_hash(oldpass, request.form.get("oldpass")):
            return apology("Incorrect old password")

        newpass = request.form.get("newpass")
        confir = request.form.get("confirmation")
        if not newpass or not confir:
            return apology("Passwords cannot be empty")
        if newpass != confir:
            return apology("Passwords do not match")

        db.execute("UPDATE users SET hash = ? WHERE id = ? ", generate_password_hash(newpass), session["user_id"])
        return redirect("/")
    else:
        return render_template("/changepass.html")

@app.route("/changeuser", methods=["GET", "POST"])
@login_required
def changeuser():
    """change password"""
    if request.method == "POST":
        pass1 = (db.execute("SELECT hash FROM users WHERE id = ?", session["user_id"]))[0]["hash"]
        if not check_password_hash(pass1, request.form.get("pass")):
            return apology("Incorrect password")

        newuser = request.form.get("newuser")
        if not newuser:
            return apology("Username cannot be empty")

        db.execute("UPDATE users SET username = ? WHERE id = ? ", newuser, session["user_id"])
        return redirect("/")
    else:
        return render_template("/changeuser.html")

@app.route("/guide")
@login_required
def guide():
    return render_template("/guide.html")

@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    if request.method == "POST":
        link = request.form.get("link")
        name = request.form.get("name")
        icon = request.form.get("options-outlined")
        renode1 = request.form.get("renodes")
        check = db.execute("SELECT name FROM links WHERE user_id = ?",session["user_id"])

        if not renode1:
            renode1= 0

        for ch in check:
            if ch["name"] == name:
                return apology("Link name already exists")

        if not icon:
            return apology("Must select an icon")

        if not link or not name:
            return apology("Link or name cannot be empty")

        if renode1 == "0":
            db.execute("INSERT INTO links (user_id,link,icon,name) VALUES (?,?,?,?)",session["user_id"],link,"/static/icons/" + icon,name)
        else:
            db.execute("INSERT INTO links (user_id,link,icon,name,node) VALUES (?,?,?,?,?)",session["user_id"],link,"/static/icons/" + icon,name,int(renode1))

        return redirect("/")
    else:
        icons = os.listdir("static/icons")
        renode = db.execute("SELECT name,id FROM renode WHERE user_id = ?", session["user_id"])
        return render_template("/add.html", renode = renode, icons = icons)

@app.route("/createnode", methods=["GET", "POST"])
@login_required
def renode():
    if request.method == "POST":

        name = request.form.get("name")
        links = request.form.getlist("links")
        check = db.execute("SELECT name FROM renode WHERE user_id = ?",session["user_id"])

        if not name:
            return apology("ReNode name cannot be empty")

        for ch in check:
            if ch["name"] == name:
                return apology("ReNode already exists")

        db.execute("INSERT INTO renode (user_id,name) VALUES (?,?)",session["user_id"],name)
        node = int(db.execute("SELECT id FROM renode WHERE user_id = ? AND name = ?",session["user_id"],name)[0]["id"])
        if not name:
            return apology("Link or name cannot be empty")

        if links:
            for link in links:
                db.execute("UPDATE links SET node = ? WHERE user_id = ? AND name = ?",node,session["user_id"],str(link))

        return redirect("/")
    else:
        link1 = db.execute("SELECT name,node FROM links WHERE user_id = ?", session["user_id"])
        renode = db.execute("SELECT name,id FROM renode WHERE user_id = ?", session["user_id"])
        return render_template("/createnode.html", links = link1, renode = renode)

@app.route("/deletelink", methods=["GET", "POST"])
@login_required
def delink():
    if request.method == "POST":
        name = request.form.get("name")
        db.execute("DELETE FROM links WHERE user_id = ? AND name = ?",session["user_id"],name)
        return redirect("/")
    else:
        return redirect("/")

@app.route("/deleterenode", methods=["GET", "POST"])
@login_required
def deren():
    if request.method == "POST":
        id = request.form.get("rename")
        db.execute("DELETE FROM renode WHERE id = ?",id)
        db.execute("UPDATE links SET node = ? WHERE user_id = ? AND node = ?",0,session["user_id"],id)
        return redirect("/")
    else:
        return redirect("/")

@app.route("/editrenode", methods=["GET", "POST"])
@login_required
def editrenode():
    if request.method == "POST":
        id = request.form.get("renodes")
        newname = request.form.get("newname")
        links = request.form.getlist("links")
        checkname = db.execute("SELECT name FROM renode WHERE user_id = ?",session["user_id"])

        if newname:
            for ch in checkname:
                if ch["name"] == newname:
                    return apology("ReNode name already exists")
            db.execute("UPDATE renode SET name = ? WHERE user_id = ? AND id = ?",str(newname),session["user_id"],id)

        if links:
            for link in links:
                db.execute("UPDATE links SET node = ? WHERE user_id = ? AND name = ?",id,session["user_id"],str(link))

        return redirect("/")
    else:
        link1 = db.execute("SELECT name,icon,node FROM links WHERE user_id = ?", session["user_id"])
        ren = db.execute("SELECT * FROM renode WHERE user_id = ?", session["user_id"])
        return render_template("/editrenode.html",links = link1, renode = ren)


@app.route("/editlink", methods=["GET", "POST"])
@login_required
def editlink():
    if request.method == "POST":
        link = request.form.get("links")
        print(link)
        name = request.form.get("newname")
        icon = request.form.get("options-outlined")
        node = request.form.get("renodes")

        if not link:
            return apology("No link selected to edit")

        checkname = db.execute("SELECT name FROM links WHERE user_id = ?",session["user_id"])

        if name:
            for ch in checkname:
                if ch["name"] == name:
                    return apology("Link name already exists")

        if not node:
            node = db.execute("SELECT node FROM links WHERE user_id = ? AND name = ?",session["user_id"],link)[0]["node"]

        if not name:
            name = link

        if not icon:
            icon = db.execute("SELECT icon FROM links WHERE user_id = ? AND name = ?", session["user_id"],link)[0]["icon"]
            db.execute("UPDATE links SET name = ?, icon = ?, node = ? WHERE user_id = ? AND name = ?",name,icon,node,session["user_id"],link)
        else:
            db.execute("UPDATE links SET name = ?, icon = ?, node = ? WHERE user_id = ? AND name = ?",name,"/static/icons/" + icon,node,session["user_id"],link)

        return redirect("/")
    else:
        link1 = db.execute("SELECT link,icon,name,node FROM links WHERE user_id = ?", session["user_id"])
        ren1 = db.execute("SELECT id,name FROM renode WHERE user_id = ?", session["user_id"])
        icons1 = os.listdir("static/icons")
        return render_template("/editlink.html",links = link1, renode = ren1, icons = icons1)