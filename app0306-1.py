from flask import Flask, render_template, request, redirect

# 객체 : 데이터 + 함수
# 클래스 : 객체를 만드는 설계도. 대문자로 시작하는데 파이썬 클래스들은 소문자로 시작
# 클래스를 가지고 객체를 만드는 함수가 클래스 이름과 같다 : 생성자 (constructor)

app = Flask(__name__)

# 안에서 만들면 서로 접근이 안되니까 global로 nums 변수 지정
nums = []

# /nums 라는 주소로 input.html를 보여주는 view 함수를 작성하시오
@app.route("/nums", methods=['get'])
def input():
    return render_template("input-1.html")

@app.route("/nums",methods=['post'])
def process():
    # get 방식은 request.args
    # post 방식은 request.form
    # methods는 보통 앞에 붙음
    value = int(request.form.get('value'))
    nums.append(value)
    return redirect("/result")
                # /result 페이지로 옮기는 작업


# 결과를 보여주는 주소 만들기

@app.route("/result")
def result():
    return render_template("result.html", nums=nums)




app.run(debug=True)


# 웹사이트 기본 작업 툴
