from flask import Flask, render_template
from todo1_view import todo01
from todo2_view import todo2
from todo3_view import todo03
from todo4_view import todo4

app = Flask(__name__)

app.register_blueprint(todo01)
app.register_blueprint(todo2)
app.register_blueprint(todo03)
app.register_blueprint(todo4)

@app.route("/")
def index():
    return render_template("index.html")

