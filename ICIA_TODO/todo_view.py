from flask import Flask, redirect, render_template, request
import datetime as dt

app = Flask(__name__)

todos = []
tno = 1

@app.route("/todo")
def todo():
  return render_template("todo/list.html", todos=todos)

@app.route("/write", methods=['post'])
def write():
  global tno
  title = request.form.get('title')
  date = dt.datetime.now().strftime("%Y-%m-%d")
  new_todo = {'tno':tno, 'title':title, 'date':date, 'finish':False}
  todos.append(new_todo)
  tno+=1
  return redirect("/todo")

@app.route("/finish", methods=['post'])
def finish():
  tno = int(request.form.get('tno'))
  for todo in todos:
    if todo['tno'] == tno:
      todo['finish'] = True
  return redirect("/todo")

@app.route("/delete", methods=['post'])
def delete():
  tno = int(request.form.get('tno'))
  for todo in todos:
    if todo['tno'] == tno:
      todos.remove(todo)
  return redirect("/todo")




app.run(debug=True)