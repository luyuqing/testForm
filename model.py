from wtforms import Form, IntegerField, StringField, validators

class UserForm(Form):
    name = StringField('name', validators=[validators.InputRequired()])
    age = IntegerField('age', validators=[validators.InputRequired()])