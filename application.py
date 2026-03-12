from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "CMS App Running on Azure"

if __name__ == "__main__":
    app.run()