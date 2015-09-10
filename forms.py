from flask_wtf import Form

from wtforms import TextField, validators


class SearchForm(Form):
    search = TextField('Search', [validators.InputRequired()])


class AddForm(Form):
    name = TextField('Name', [validators.InputRequired()])
    key = TextField('Key', [validators.InputRequired()])
    value = TextField('Value', [validators.InputRequired()])

