from flask import Flask, Blueprint, render_template

todo03 = Blueprint('todo3', __name__, url_prefix='/todo3')

todos = [{'tno':1, 'title':'전투체육', 'date': '2025-03-12'}, 
         {'tno':2, 'title':'미용실방문', 'date': '2025-03-12'}]

@todo03.route('/list')
def list():
    count = len(todos)
    return render_template('todo3/list.html', todos = todos, count = count)



