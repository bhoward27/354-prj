from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from mysql import connector

from py.model.executor import Executor
exec = Executor()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'c14c7141e792cbae4abfc4ddbbd9b048'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # TODO: run this in executor.py
        query = "SELECT MAX(lib_card_num) from Member"
        exec.cursor.execute(query)
        lib_card_num = int(exec.cursor[0][0])+1

        # Check for NULL values and add default values
        if not form.mName.data:
            form.mName.data = None
        status, fines = 1, 0

        exec.insert('Member', (str(lib_card_num), form.address.data,
                    form.email.data, form.password.data, status, fines,
                    form.fName.data, form.mName.data, form.lName.data))

        flash('Account created for %s %s!' %
              (form.fName.data, form.lName.data), 'success')

        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # TODO: Check login data from sql database
        if form.email.data == 'a@a.a' and form.password.data == 'a':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/books')
def books():
    return catalog('Book', 'ISBN13')

@app.route('/cds')
def cds():
    return catalog('CD', 'ISSN')

@app.route('/dvds')
def dvds():
    return catalog('DVD', 'ISSN')

def catalog(itemType, query):
    query = ("SELECT %s, item.* " % query
             + "FROM %s " % itemType
             + "JOIN item ON item.item_id=%s.item_id" % itemType)
    
    exec.cursor.execute(query)
    return render_template('catalog.html', title=itemType + 's',
                           cols=exec.cursor.column_names, items=exec.cursor)


if __name__ == '__main__':
    app.run(debug=True)
