from flask_wtf import Form

from wtforms import TextField, validators


class SearchForm(Form):
    search = TextField('Search', [validators.InputRequired()])
