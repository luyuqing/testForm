from wtforms import Form, IntegerField, StringField, validators, SubmitField


class UserForm(Form):
    name = StringField('name', validators=[validators.InputRequired()])
    # age = IntegerField('age', validators=[validators.InputRequired()])
    submit1 = SubmitField('submit1')
    # submit2 = SubmitField('submit2')