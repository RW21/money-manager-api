from datetime import date

from flask import Flask, request, render_template, flash
from sheet import Entry, categories, add_entry

app = Flask(__name__)


@app.route('/')
def hello():
    return "hello"


@app.route('/entry', methods=['GET'])
def entry_page():
    return render_template('index.html', categories=categories)


@app.route('/entry', methods=['POST'])
def new_entry():
    category_parent, category_child = request.form['category'].split(', ')
    print(request.form)
    if 'income' not in request.form:
        is_income = False
    else:
        is_income = request.form['income'] == 'on'

    entry = Entry(date=date.today(),
                  is_income=is_income,
                  category_parent=category_parent,
                  category_child=category_child,
                  amount=int(request.form['amount']),
                  description=request.form['description'])
    add_entry(entry)
    flash('Successfully added')
    return render_template('index.html', categories=categories)


@app.route('/categories', methods=['GET'])
def get_entries():
    return categories


if __name__ == "__main__":
    app.run(host='0.0.0.0')
