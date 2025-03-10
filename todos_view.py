# 사용자 입출력하는 함수 : 자바는 Controller, 파이썬은 View

from flask import Blueprint, render_template, redirect, request, session
import datetime as dt
#                ㄴ datetime이 기니까 dt라고 줄여서 부르는 것 같음


# Blueprint로 현재 뷰 소스의 청사진을 찍어서 외부로 내보낸다
# todos_app : 외부로 내보내는 이름
# 'todos_app' : 별칭. 우리는 사용 예정 x

todos_app = Blueprint('todos_app', __name__)

todos = []
tno = 1

@todos_app.route("/")
def index():
  return render_template("list.html", todos=todos)

@todos_app.route("/write", methods=['post'])
def write():
  global tno
  # 초간단 로그인 구현 : 세션에 로그인한 아이디를 저장
  # 세션은 사용자 정보를 저장하는 서버측 공간 (사용자마자 1개씩)
  # 세션에 저장하면 프로그램 전체에서 사용이 가능함  
  login_id = session.get('username')      # 로그인 아이디를 꺼내는 방법 중 하나
  # 로그인 안 했으면 /로 이동
  if login_id==None :         # login_id 의 값이 None 이라면
    return redirect("/")  # "/" (index) 로 이동하라
  title = request.form.get('title')         # title 꺼내기
  # 날짜를 특정한 패턴의 문자열로 변환한다
  date = dt.datetime.now().strftime('%Y-%m-%d')
  new_todo= {'tno':tno, 'title':title, 'writer':login_id, 'date':date, 'finish':False}
  todos.append(new_todo)    # ㄴ new_todo 라는 새로운 변수로 할 일을 주기
  tno+=1        # ㄴ todos에 new_todo 추가하기
    # ㄴ tno 증가시키기
  return redirect("/")

@todos_app.route("/finish", methods=['post'])
def finish():
  # 로그인 안 했으면 루트로 보내버려
  login_id = session.get('username')
  if login_id==None:
    return redirect("/")
  tno=int(request.form.get('tno'))
  # 할일을 찾아서 할일 작성자라면 (할일의 writer가 현재 로그인한 사용자)
  for todo in todos:
    if todo['tno']==tno and todo['writer']==login_id:
      todo['finish']=True
    return redirect("/")


@todos_app.route("/delete", methods=['post'])
def delete():
  login_id = session.get('username')
  if login_id==None:
    return redirect("/")
  tno= int(request.form.get('tno'))
  for todo in todos:
    if todo['tno']==tno and todo['writer']==login_id:
      todos.remove(todo)
  return redirect("/")
      