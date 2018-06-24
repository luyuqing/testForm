from flask import Flask, render_template, request

from model import UserForm


app = Flask(__name__)

@app.route('/')
def index():
    form_fields = UserForm(request.form)
    return render_template("view.html", form_fields=form_fields)

if __name__ == '__main__':
    app.run(debug=True)