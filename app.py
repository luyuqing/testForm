from flask import Flask, render_template, request, jsonify
from werkzeug.datastructures import MultiDict

from model import UserForm


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserForm()
    if request.method == 'POST':
        m = MultiDict([('name', 'lala')])
        form = UserForm(m)

    return render_template("view.html", form=form)


@app.route('/hello', methods=['POST'])
def hello():
    name = request.form['name']
    new = 'hello ' + name
    return jsonify({"new": new})

# @app.route('/show', methods=['POST'])
# def show():
#     form = UserForm(request.form)
#     name = form.name.data
#     age = form.age.data
#     return jsonify({"name": name, "age": age})


# if request.method == 'POST':
#         m = MultiDict([("name", "lala"), ("age", 3)])
#         form = UserForm(m)
#         return jsonify(dict(m))
#     return render_template("view.html", form=form)
if __name__ == '__main__':
    app.run(debug=True)
