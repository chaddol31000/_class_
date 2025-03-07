# 명함관리
# 명함 : 이름과 연락처 -> {'name':'홍길동', 'tel':'1234'}
# 명함 리스트, 명함 추가, 명함 삭제

from flask import Flask, redirect, render_template, request

#__name__은 현재 실행중인 모듈의 이름을 나타내는 내장변수
# 모듈 이름을 이용해서 templates, static 등을 관리한다
app = Flask(__name__)

# 실제 저장은 외부의 오라클을 사용할 것이다 (연습용)
name_cards=[{'name': '홍길동', 'tel':'1234'},{'name':'전우치', 'tel':'2345'}]
# 404는 찾지 못해서 실패한 것
# 현재 경우 favicon.ico 에서 404가 뜬다
# 그 이유는 아이콘을 불러오지 못해서 그런 거임
# 405 = method 오류

@app.route("/card/list")
def list():
    return render_template("card/list.html", name_cards=name_cards)

@app.route("/card/insert", methods=['post'])
def insert():
    name = request.form.get("name", None)
    tel = request.form.get("tel", None)
    new_card={'name':name, 'tel':tel}
    name_cards.append(new_card)
    return redirect("/card/list")


@app.route("/card/delete", methods=['post'])
def delete():
    name = request.form.get("name", None)
    for card in name_cards:
        if card['name']==name:
            name_cards.remove(card)
    return redirect("/card/list")    

app.run(debug=True)