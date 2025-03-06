from flask import Flask, render_template, redirect, request

app = Flask(__name__)

sum_result = 0
# global로 해도 되지만 문제가 많을 수 있음 (global이 하나면 여러 사용자가 다같이 쓰기에 덮어씀 그래서 애매해짐)
# 나중에 session 이라는 명령어로 할 수 있음

@app.route("/add", methods=['get'])
def add_get():
    return render_template("add.html")

@app.route("/add", methods=['post'])
def add_post():
    global sum_result
    num1= int(request.form.get('value1'))
    num2= int(request.form.get('value2'))
    sum_result = num1+num2
    return redirect("/result")

@app.route("/result")
def result():
    global sum_result
    return render_template("result.html", result=sum_result)


app.run(debug=True)