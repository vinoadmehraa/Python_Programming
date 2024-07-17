from flask import Flask
"""
This create an instance of flask app class,
which would be WSGI (web server gateway interface) application.
"""

## WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my Flask course. and, this is amazing edit."

@app.route("/index")
def index():
    return "This is index page."



if __name__ == "__main__":
    app.run(debug=True)