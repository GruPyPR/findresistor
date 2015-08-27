from flask import Flask
from flask import render_template

from forms import SearchForm


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super_secret_key'


@app.route("/")
def home():
    return "Home"


@app.route("/search/", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    return render_template('search.html', form=form)


@app.route("/add/")
def add():
    return "Add"


if __name__ == "__main__":
    app.run()
