from flask import Flask
app = Flask(__name__)

@app.route("/info")
def test_main():
    return "요청을 접수했습니다"

app.run(debug=True)

# flask는 파이썬을 통해 내용을 만들어 웹으로 보내는 동적임
# 이름을 원하는 것으로 바꿀 수 있음