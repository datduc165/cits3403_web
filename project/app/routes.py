from flask import render_template
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse

from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Post

'''two @app.route spectify that whenever the browser access URL associated with / or index, it will return the string of the following function to the browser as a respone'''
@app.route('/')
def base():
    return render_template('base.html',title="Base")

@app.route('/index')
@login_required
def index():
    posts=Post.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html',title="HomePage", posts=posts)

@app.route('/test')
def test():
    return render_template('test.html',title="TestPage")

'''methods tell that this function accppet GET and POST method'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
       
    return render_template('login.html', title='Sign In', form_html=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user', methods=['GET', 'POST'])
@login_required
def user():
    u = User.query.all()
    if request.method == "POST":
        data = request.form['type']
        pet = request.form['pet']
        print('Got some thing gonna print it now....')
        print(data)
        print('Favourite pet hey....')
        print(pet)
        print('ADd to our post')
        p=Post(body=data, author=current_user)
        print('New posts body here')
        print(p.body)
        db.session.add(p)
        db.session.commit()
    return render_template('user.html',title='U.U', u = u)

1