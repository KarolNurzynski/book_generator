from app import create_app
from flask import render_template

app = create_app('flask.cfg')

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html", title="Home")

if __name__ == '__main__':  
    app.run(host='0.0.0.0', debug=False)