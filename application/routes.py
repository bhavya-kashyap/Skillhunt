from application import app
from flask import render_template, url_for, flash, redirect
from application.forms import RegistrationForm, LoginForm, OtpForm
import application.otp as otp
from application.models import User, JobPost

app.config['SECRET_KEY'] = 'skillhunt'

@app.route("/")
@app.route("/index.html")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/contact")
@app.route("/contact.html")
def contact():
    return render_template('contact.html')

@app.route("/blog1")
@app.route("/blog1.html")
def blog1():
    return render_template('blog1.html')

@app.route("/blog2")
@app.route("/blog2.html")
def blog2():
    return render_template('blog2.html')

@app.route("/blog3")
@app.route("/blog3.html")
def blog3():
    return render_template('blog3.html')

@app.route("/blog4")
@app.route("/blog4.html")
def blog4():
    return render_template('blog4.html')

@app.route('/signup', methods=['GET', 'POST'])
@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.name.data} with contact number {form.contact.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('signup.html', form = form)

@app.route('/login', methods=['GET', 'POST'])
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        a = otp.generate_otp(int(form.contact.data))
        print(a)
        return redirect(url_for('otpverify'))
    return render_template('login.html', form = form)

@app.route('/otp', methods=['GET', 'POST'])
@app.route('/otp.html', methods=['GET', 'POST'])
def otpverify():
    form = OtpForm()
    if form.validate_on_submit():
        if otp.verify_otp(int(form.otp.data)):
            flash(f'Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash(f'Enter the correct otp', 'failure')
    return render_template('otpverify.html', form = form)