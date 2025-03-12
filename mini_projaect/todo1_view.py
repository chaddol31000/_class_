from flask import Flask, Blueprint, render_template, redirect, request

todo01 = Blueprint('todo1', __name__, url_prefix='/todo1')
todos=[{'tno':1, 'title':'전투체육', 'date':'2025-03-12'},
       {'tno':2, 'title':'미용실 방문', 'date':'2025-03-12'}]

@todo01.route("/list")
def list():
  count = len(todos)
  return render_template("todo1/list.html", todos=todos, count=count)





