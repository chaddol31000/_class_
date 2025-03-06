from flask import Flask, render_template, redirect, request
                          # 자바에서는 foward
app = Flask(__name__)

# flask 문서에서 주소가 같으면 안되지만 methods 가 다르다면 같아도 됨
# get 방식은 다 render_template
# post 방식은 다 redirect

@app.route("/login", methods=['get'])
def login_get():
    state = request.args.get('state', None)
    message = "로그인에 실패했습니다" if state!=None else ""
    return render_template("login.html", message=message)

@app.route("/login", methods=['post'])
def login_post():
    username=request.form.get("username")
    password=request.form.get("password")
    if username=='spring' and password=='1234':
        return redirect("/success")
    else:
        return redirect("login?state=fail")

@app.route("/success")
def success():
    return render_template("success.html")


app.run(debug=True)