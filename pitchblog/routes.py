from flask import render_template,url_for,flash,redirect
from pitchblog import app,db,bcrypt
from  pitchblog.forms import RegistrationForm,LoginForm
from pitchblog.models import User,Post




posts = [
    {
        'author':'Mary Jane',
        'title':'Blog Pitch 1',
        'content':'First post content',
        'date_Posted':'April 29,2019'
    },
     {
        'author':'Mary Jane',
        'title':'Blog Pitch 2',
        'content':'second post content',
        'date_Posted':'April 29,2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'mary@gmail.com' and form.password.data == '1234':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
