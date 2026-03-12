from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("posts.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/create")
def create():
    return render_template("edit.html")

if __name__ == "__main__":
    app.run()