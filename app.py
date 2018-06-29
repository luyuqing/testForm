from flask import Flask, render_template, request, jsonify, redirect

from model import UserForm, ImportForm, AnswerForm


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    import_form = ImportForm()
    user_form = UserForm()
    answer_form = AnswerForm()
    if request.method == 'POST':
        if 'submit1' in request.form:
            file_name = request.form['file_name']
            if file_name == 'f1':
                fill_data = {'name': 'lalala', 'hobby': 'karate'}
                user_form = UserForm(data=fill_data)
            elif file_name == 'f2':
                fill_data = {'name': 'keke', 'hobby': 'swim'}
                user_form = UserForm(data=fill_data)
            else:
                pass
        else:
            name = request.form['name']
            hobby = request.form['hobby']
            user_form = UserForm(data={'name': name, 'hobby': hobby})
            new = 'hello ' + name + ' likes ' + hobby
            answer_form = AnswerForm(data={'answer': new})
    return render_template("view.html", import_form=import_form, user_form=user_form, answer_form=answer_form)


@app.route('/save', methods=['POST'])
def save_file():
    name = request.form['name']
    hobby = request.form['hobby']
    print("#####################")
    print(name)
    final = name + hobby
    with open("file.text", "w") as f:
        f.write(final)
    return jsonify({"name": name, "hobby": hobby})

# not necessary anymore
@app.route('/import/<filename>', methods=['GET', 'POST'])
def import_file(filename):
    import_form = ImportForm()

    if filename == 'f1':
        fill_data = {'name': 'lalala', 'hobby': 'karate'}
        user_form = UserForm(data=fill_data)
    elif filename == 'f2':
        fill_data = {'name': 'keke', 'hobby': 'swim'}
        user_form = UserForm(data=fill_data)
    else:
        user_form = UserForm()
    answer_form = AnswerForm()
    if request.method == 'POST':
        name = request.form['name']
        hobby = request.form['hobby']
        user_form = UserForm(data={'name': name, 'hobby': hobby})
        new = 'hello ' + name + 'likes ' + hobby
        answer_form = AnswerForm(data={'answer': new})
    return render_template("view.html", import_form=import_form, user_form=user_form, answer_form=answer_form)


# not necessary anymore
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    name = request.form['name']
    new = 'hello ' + name
    return jsonify({"new": new})

if __name__ == '__main__':
    app.run(debug=True)
