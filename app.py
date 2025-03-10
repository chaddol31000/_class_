from flask import Flask, session,redirect
from todos_view import todos_app

app = Flask(__name__)

#세션 암호화를 위한 비밀번호 지정 (무조건 해야하는 거 아니고 flask 에서만 해야함)
app.config['SECRET_KEY']='1234'


app.register_blueprint(todos_app)      # 확장

# 테스트용 로그인, 로그아웃 함수 -> get 처리 (가짜로 만들고 지워야함)
# 권장되지는 않지만 앞순서를 기다리기에 시간이 없기에 가짜로 만들고
# 다 만들면 지워서 정리 
# 팀 프로젝트는 git main 사용해서 하고 branch는 사용하지 않을 거임


@app.route("/spring")
def test_spring_login():
  session['username']='spring'
  return redirect("/")

@app.route("/summer")
def test_summer_login():
  session['username']='summer'
  return redirect("/")

@app.route("/logout")
def test_logout():
  session.clear()
  return redirect("/")


app.run(debug=True)