from flask import Flask, render_template, flash, redirect, url_for, logging, request, session
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'project'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
print(mysql)


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/books/<string:id>/')
def book(id):
    details = {
        'author': 'authors',
        'genre': 'bookgenre'
    }
    return item('bookISBN', 'Book', 'ISBN13', id, details)


@app.route('/cds/<string:id>/')
def cd(id):
    details = {
        'artist': 'cdartist',
        'genre': 'cdgenre'
    }
    return item('cdISSN', 'CD', 'ISSN', id, details)


@app.route('/dvds/<string:id>/')
def dvd(id):
    details = {
        'actor': 'dvdactors',
        'director': 'dvddirectors',
        'genre': 'dvdgenre'
    }
    return item('dvdISSN', 'DVD', 'ISSN', id, details)


def item(item, table, pk, id, details):
    cur = mysql.connection.cursor()
    query = (
        f"SELECT item_id, {table}.* FROM item"
        f" JOIN {table} ON {item}={pk}"
        f" WHERE item_id={id}")
    cur.execute(query)
    res = cur.fetchone()

    for det in details:
        query = (
            f"SELECT {det} FROM {details[det]}"
            f" WHERE {item} IN ("
            f"SELECT {pk} FROM {table}"
            f" JOIN item ON {item}={pk}"
            f" WHERE item_id={id})"
        )
        cur.execute(query)
        details[det] = cur.fetchall()

    return render_template('item.html', title=res['title'], item=res, details=details)


class RegisterForm(Form):
    name = StringField('First Name', [validators.Length(min=1, max=20)])
    lastname = StringField('Last Name', [validators.Length(min=1, max=20)])
    phone = StringField('Phone', [validators.Length(min=0, max=10)])
    address = StringField('Address', [validators.Length(min=1, max=50)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [validators.DataRequired(),
                                          validators.EqualTo('confirm', message="The entered passwords do not match")])
    confirm = PasswordField('Confirm Password')


@app.route('/register', methods=['GET', "POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        lastname = form.lastname.data
        address = form.address.data
        email = form.email.data
        password = form.password.data

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Member(address, email, password, fName, lName) VALUES(%s,%s,%s,%s, %s)",
                    (address, email, password, name, lastname))

        mysql.connection.commit()
        cur.close()
        flash("You are now registed and can log in", 'Success')
        redirect(url_for('index'))
    return render_template('Register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        #        #get form fields
        email = request.form['email']
        password_cadidate = request.form['password']
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM Member WHERE email=%s", [email])
        if result > 0:
            data = cur.fetchone()
            password = data['password']
            if password_cadidate == password:
                app.logger.info('PASSWORD MATCHED')
            else:
                error = "invalid log in"
                return render_template('login.html', error=error)
        else:
            error = 'User not found'
            return render_template('login.html', error=error)
    return render_template('login.html')


@app.route('/books')
def books():
    return catalog('bookISBN', 'Book', 'ISBN13')


@app.route('/cds')
def cds():
    return catalog('cdISSN', 'CD', 'ISSN')


@app.route('/dvds')
def dvds():
    return catalog('dvdISSN', 'DVD', 'ISSN')


def catalog(item, table, pk):

    query = (
        f"SELECT item_id, {table}.* FROM item"
        f" JOIN {table} ON {item}={pk}"
        f" ORDER BY item_id")

    cur = mysql.connection.cursor()
    cur.execute(query)
    res = cur.fetchall()
    for item in res:
        print(item)
        for i in item:
            print(i)
            print(item[i])
    return render_template('catalog.html', title=f'{table}s', results=res)


app.secret_key = '123412312321'
if __name__ == '__main__':
    app.run(debug=True)
