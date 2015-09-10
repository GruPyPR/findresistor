from flask import Flask
from flask import render_template

from flask.ext.elasticsearch import FlaskElasticsearch

from forms import SearchForm, AddForm


app = Flask(__name__)
es = FlaskElasticsearch(app)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super_secret_key'


@app.route("/")
def home():
    return "Home"


@app.route("/search/", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    return render_template('search.html', form=form)


@app.route("/add/", methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        data = {
            'name': form.name.data,
            'key': form.key.data,
            'value': form.value.data,
        }
        response = es.index(index='resistor', doc_type='component',
                            body=data)
        if not response['created']:
            return 'Error'
        else:
            return 'Success'
    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run()
