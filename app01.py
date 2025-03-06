# 기능들의 집합 : 라이브러리 (library)
# import없이 사용가능한 것들 : 내장~

# 보통의 경우 라이브러라고 하면 추가로 설치해서 사용한다
# 라이브러리 : 단순한 기능의 집합
# 프레임워크 : 라이브러리 + 사용법

# 웹 프레임워크 : 사용자 요청 -> 처리 -> 사용자에게 응답

# 파이썬의 웹 프레임워크 : flask, django, fast api (fast api는 진짜 개같다고 하심)
# 자바의 웹 프레임워크 : spring

# 클래스 이름은 대문자로 시작하지만,
# 파이썬이 제공하는 클래스들은 소문자로 시작하는 경우도 있다

# 이 과정은 항상 있어야 하기에 복붙이 가능함
from flask import Flask

# Flask 앱을 생성. (현재 모듈의 이름을 가지고 생성함)
# python app01.py 이렇게 직접 실행한 경우 __name__은 "__main__"이 된다
# controller : 자바 용어로 사용자 요청을 접수하는 것
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Flask"

@app.route("/test1")
def test1():
    return "테스트 1번입니다."

# /test2로 요청이 들어오면 "테스트 2번입니다"라고 응답하도록
# 컨트롤러 함수를 작성하고 웹브라우저로 접근하시오

@app.route("/test2")
def test2():
    return "테스트 2번입니다."


if __name__ == '__main__':
    app.run(debug=True)


