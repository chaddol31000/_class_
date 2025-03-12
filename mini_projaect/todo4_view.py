from flask import Flask, Blueprint, render_template

todo4 = Blueprint('todo4', __name__, url_prefix='/todo4')

todos = [{'tno':1, 'title':'전투지옥', 'date':'2025-03-12'},
         {'tno':2, 'title':'미용실 방문', 'date':'2025-03-12'}]
@todo4.route("/list")
def list():
    count = len(todos)
    return render_template("todo4/list.html", todos=todos, count=count)