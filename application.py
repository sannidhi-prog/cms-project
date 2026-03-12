from flask import Flask, render_template, request, redirect
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def home():
    return redirect("/posts")

@app.route("/login")
def login():
    return "Login Page"

@app.route("/posts")
def posts():
    return "Posts Page"

@app.route("/create")
def create():
    return "Create Post Page"

@app.route("/edit/<id>")
def edit(id):
    return f"Edit post {id}"

if __name__ == "__main__":
    app.run()