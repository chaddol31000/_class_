from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/add", methods=['get'])
def add_get():
    return render_template("add.html")

@app.route("/add", methods=['post'])
def add_post():
    value1= int(request.form.get('value1'))
    value2= int(request.form.get('value2'))
    sum_result = value1+value2
    return redirect(f"/result?sum_result={sum_result}")

@app.route("/result")
def result():
    sum_result = request.args.get("sum_result")
    return render_template("result.html", sum_result=sum_result)


app.run(debug=True)