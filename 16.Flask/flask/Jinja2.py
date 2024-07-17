## Building url dynamically

## Variable rules

## Jinja2 template engine
"""
{{ }} - expression to printout in html.
{%...%} - conditions, for loops.
{#...#} - this is for comments.
"""


from flask import Flask, render_template, request
"""
This create an instance of flask app class,
which would be WSGI (web server gateway interface) application.
"""

## WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to my 1st Flask application</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=="POST":
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')
    
## variable rule
@app.route("/success/<int:score>")
def success(score):
    #return "The marks you got is: " + str(score)
    res=""
    if score>=50:
        res="Passed"
    else:
        res="Failed"
    
    return render_template("results.html", results=res)


## variable rule
@app.route("/successres/<int:score>")
def successres(score):
    #return "The marks you got is: " + str(score)
    res=""
    if score>=50:
        res="Passed"
    else:
        res="Failed"
    
    exp={'score':score, "res":res}

    return render_template("results_1.html", results=exp)







if __name__ == "__main__":
    app.run(debug=True)