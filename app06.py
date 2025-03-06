# 숫자 2개를 입력 받아 덧셈 결과를 출력하기

from flask import Flask, render_template, request

app = Flask(__name__)

# 입력
@app.route("/input")
def input():
    return render_template("input.html")

# 출력
# 숫자 입력 받을 때 int 씌우는 거 잊지 말기
# 더하거나 곱하는 값은 여기 def 에서 처리하기
# result=result 가 오는 이유 알기


@app.route("/out")
def out():
    value1= int(request.args.get('value1'))
    value2 = int(request.args.get('value2'))
    result = value1+value2
    return render_template("out.html", result=result)

app.run(debug=True)