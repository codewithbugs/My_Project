from application import app, bcrypt, LoginManager
from flask import render_template, url_for, flash, redirect
from application.forms import LoginForm
from application.models import Emp
from flask_login import login_user,current_user

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/files")
def files():
    return render_template("files.html")

@app.route('/', methods=['GET', 'POST'])
@app.route("/login", methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		emp = Emp.query.filter_by(empname=form.username.data).first()
		if emp and (emp.emppass == form.password.data):
			login_user(emp, remember=form.remember.data)
			return redirect(url_for('home'))
		else:
			flash('Login Unseccessful. Please check name and password','danger')

	return render_template('login.html',title='login',form=form)