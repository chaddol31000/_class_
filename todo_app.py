from flask import Flask, render_template, redirect, request
import datetime
app = Flask(__name__)

todos=[
        {'tno':1, 'title':'치킨데이', 'date':'2025-03-07', 'finish':False},
        {'tno':2, 'title':'소맥데이', 'date':'2025-03-07', 'finish':True}
      ]
      #               본문                                  마감일(False or True)
tno = 3
@app.route("/todo/list")
def list():
  return render_template("todo/list.html", todos=todos)

@app.route("/todo/insert", methods=['post'])
def insert():
  global tno
  title=request.form.get("title")
  date_str = datetime.datetime.now().strftime("%Y-%m-%d")
  new_todo={'tno':tno, 'title':title, 'date':date_str,'finish':False}
  todos.append(new_todo)
  tno+=1
  return redirect("/todo/list")

@app.route("/todo/toggle", methods=['post'])
def toggle():
  tno= int(request.form.get('tno'))
  for todo in todos:
    if todo['tno']==tno:
      todo['finish'] = not todo['finish']
  return redirect("/todo/list")

@app.route("/todo/delete", methods=['post'])
def delete():
  tno= int(request.form.get('tno'))
  for todo in todos:
    if todo['tno']==tno:
      todos.remove(todo)
  return redirect("/todo/list")

app.run(debug=True)