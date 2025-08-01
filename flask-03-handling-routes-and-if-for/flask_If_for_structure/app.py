# Import Flask modules
from flask import Flask, render_template

# Create an object named app 
app = Flask(__name__)


# Create a function named head which shows the massage as "This is my first conditions experience" in `index.html` 
# and assign to the route of ('/')
@app.route("/")
def head():
    message="This is my first conditions experience"
    return render_template("index.html", message=message)


# Create a function named header which prints numbers elements of list one by one in `body.html` 
# and assign to the route of ('/')
@app.route("/list")
def header():
    names = ["Jane", "Loius", "Ida", "Kwame", "Sara"]
    return render_template("body.html", object=names)


# run this app in debug mode on your local.
if __name__=="main":
    app.run(debug=True)
