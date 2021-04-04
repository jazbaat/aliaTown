from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.secret_key = "Pakistan"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shaheer.db"
db = SQLAlchemy(app)



class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(80))
    select = db.Column(db.String(80))
    contact = db.Column(db.String(80))
    time = db.Column(db.DateTime, default=datetime.now())
    callme = db.Column(db.String(80))







@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        todo = request.form["todo"]
        session["todo"] = todo
        contact = request.form["contact"]
        session["contact"] = contact
        select = request.form["select"]
        session["select"] = select
        callme = request.form["callme"]
        session["callme"] = callme

        x = Data(todo=todo, contact=contact, select=select, callme=callme)
        db.session.add(x)
        db.session.commit()
        return redirect(url_for("user"))
        
    return redirect(url_for("user"))


@app.route("/account")
def account():
    c = Data.query.all()
    return render_template("account.html", c=c)




@app.route("/humanity")
def humanity():
    return render_template("humanity.html")



@app.route("/user")
def user():
    y = Data.query.all()
    return render_template("todo.html", y=y)


@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)