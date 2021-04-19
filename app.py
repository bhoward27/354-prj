from flask import Flask, render_template, flash, redirect, url_for, logging, request, session
from books import Books
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
Books = Books()


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/books')
def books():
    return render_template('Books.html', books=Books)


@app.route('/book/<string:id>/')
def book(id):
    return render_template('Book.html', id=id)


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
                error="invalid log in"
                return render_template('login.html', error=error)
        else:
            error='User not found'
            return render_template('login.html', error=error)
    return render_template('login.html')


app.secret_key = '123412312321'
if __name__ == '__main__':
    app.run(debug=True)
