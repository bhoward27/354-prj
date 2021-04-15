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
        for row in exec.cursor:
            print(row)
            lib_card_num = int(row[0])+1
            print(lib_card_num)

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
    query = """
SELECT book.ISBN13, item.*
FROM project.book
JOIN project.item ON item.item_id=book.item_id
"""

    exec.cursor.execute(query)
    
    print(exec.cursor.column_names)
    print(exec.cursor.column_names.index('ISBN13'))
    # for book in exec.cursor:
    #     print(book)
    return render_template('books.html', title='Books',
                           cols=exec.cursor.column_names, books=exec.cursor)


if __name__ == '__main__':
    app.run(debug=True)
