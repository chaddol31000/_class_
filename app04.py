from flask import Flask, request

app = Flask(__name__)

# test1 주소로 value라는 숫자를 받아오시오 (문자열)
# value*value를 해서 출력하시오

# request.args.get
# request.get.parameter
# location.search

@app.route("/test1")
def test1():
    value = int(request.args.get("value",'10'))
    value = value*value
    return f'제곱값 : {value}'

app.run(debug=True)