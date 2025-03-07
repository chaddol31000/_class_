from flask import Flask, redirect, render_template, request

app = Flask(__name__)

name_cards=[{'cno':1,'name':'spring','tel':'1234'},{'cno':2, 'name':'summer','tel':'2345'}]
cno=3

@app.route("/card/list")
def list():
  error = request.args.get('error')
  message=''
  if error=='insert':  # 'insert' 에 에러가 있다면 메세지를 출력하라 아니면 list.html로 이동하라
    message= '연락처가 이미 존재합니다'
  elif error=='delete':
    message= '연락처를 찾을 수 없습니다' # 'delete'에 에러가 있다면 메세지를 출력 아니면 list.html로 이동
  return render_template("card2/list.html", name_cards=name_cards, message=message)


@app.route("/card/insert", methods=['post'])
def insert():
  global cno     # 번호를 글로벌로 불러오기
  name=request.form.get('name', None)
  tel= request.form.get('tel', None)
  # 중복이면 에러 처리 (이름과 연락처가 모두 중복이면 에러 코드를 가지고 /card/list로 이동)
  for card in name_cards:  # 모든 명함에 대해서 중복된 명함이 있다면 중지하고 에러코드로 이동하기
    if card['name']==name and card['tel']==tel:
      return redirect("/card/list?error=insert")   # 비정상적인 상황
  new_card = {'cno':cno,'name':name,'tel':tel}
  name_cards.append(new_card)
  cno+=1    # 글로벌로 부른 cno를 증가시키기
  return redirect("/card/list")       # 정상적인 상황

@app.route("/card/delete", methods=['post'])
def delete():
  # 없으면 어떡하지 -> 오류처리
  cno = int(request.form.get('cno'))
  for card in name_cards:
    if card['cno'] == cno:
      name_cards.remove(card)
      return redirect("/card/list")
  return redirect("/card/list?error=delete") # 에러가 뜬다는 주소를 만들어 출력이 가능함

# 리스트는 값을 바꿀 수 있지만, 정수나 실수는 값을 바꿀 수 없음
# 그래서 정수나 실수인 변수는 글로벌 함수로 불러와야함
# 마이크로 프레임워크 
# 하늘색 - 변수 / 노란색 - 파이썬 명령어 / 빨간색 - 문자열 / 파란색 - 함수
# redirect는 주소이기 때문에 무조건 /로 시작해야함

app.run(debug=True)