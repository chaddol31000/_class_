# 웹서버 : 정적인 파일을 응답
# WAS : 파이썬을 실행해서 동적으로 만들어서 응답
# 파이썬 설치 -> 실행 -> 확인
# pip install flask

# my_mall
# ㄴ templates : html
# ㄴ static : css.js

# 위처럼 작업해야 편함 (프레임워크가 이렇게 정해줌)

# 함수들을 자바는 controller 함수, 파이썬은 view 함수라고 불림

from flask import Flask, render_template, request
app= Flask(__name__)

# 숫자 입력화면을 띄움
@app.route("/start")
def start():
    return render_template("start.html")

# 입력한 결과를 출력
@app.route("/end")
def end():
    value = request.args.get('value')
    result= value+value
    return render_template("end.html", result=value)

app.run(debug=True) 
