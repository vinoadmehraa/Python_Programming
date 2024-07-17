from flask import Flask, render_template
"""
This create an instance of flask app class,
which would be WSGI (web server gateway interface) application.
"""

## WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to my Flask course.</H1></html>"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)