from flask import Flask

app = Flask(__name__)


@app.get('/welcome')
def welcome_view():
    html = "<html><h1>welcome</h1></html>"
    return html

@app.get('/welcome/home')
def welcome_home():
    html = "<html><h1>welcome home</h1></html>"
    return html

@app.get('/welcome/back')
def welcome_back():
    html = "<html><h1>welcome back</h1></html>"
    return html