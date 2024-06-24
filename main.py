from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    with open("templates/index.html", 'rb') as f:
        contents = f.read()
        return contents


app.run(debug=True, port=5501)
