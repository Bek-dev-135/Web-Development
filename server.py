from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<username>")
def show_name(username=None):
    return render_template('index.html', name= username)
@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/blog")
def blog():
    return "<p>These is a blog</p>"