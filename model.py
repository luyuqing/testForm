from wtforms import Form, IntegerField, StringField, \
    validators, SubmitField, TextAreaField, SelectField


class ImportForm(Form):
    file_name = SelectField('file', choices=[(None, None),
                                             ('f1', 'f1'),
                                             ('f2', 'f2')])
    submit1 = SubmitField('submit1')


class UserForm(Form):
    name = StringField('name', validators=[validators.InputRequired()])
    hobby = SelectField('hobby', choices=[('swim', 'swim'),
                                          ('karate', 'karate')])
    submit2 = SubmitField('submit2')


class AnswerForm(Form):
    answer = TextAreaField('answer')
