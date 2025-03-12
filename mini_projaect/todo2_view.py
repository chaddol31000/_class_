from flask import Flask, Blueprint, render_template

todo2 = Blueprint('todo2', __name__, url_prefix='/todo2')

todos = [{'tno': 1, 'title':'잠자기', 'date':'2025-03-12'},
         {'tno': 1, 'title':'미용실', 'date':'2025-03-12'}]
@todo2.route("/list")
def list():
    count = len(todos)
    return render_template("todo2/list.html", todos = todos, count = count)




