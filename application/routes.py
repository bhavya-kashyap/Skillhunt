from application import app, db
from flask import render_template, url_for, flash, redirect, session
from application.forms import RegistrationForm, LoginForm, OtpForm, NewPostForm
import application.otp as otp
import jobquery
from application.models import User, JobPost, load_user
#from flask_login import login_user, current_user, logout_user, login_required

app.config['SECRET_KEY'] = 'skillhunt'

def check_session(func):
    if session['anonymous_user_contact']:
        def inner():
            func()
            return inner

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
    if session['anonymous_user_contact']:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, contact=form.contact.data, location=form.location.data, category=form.category.data, education=form.education.data, description=form.description.data)
        session['anonymous_user_id'] = user.id
        session['anonymous_user_contact'] = user.contact
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.name.data} with contact number {form.contact.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('signup.html', form = form)

@app.route('/login', methods=['GET', 'POST'])
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if session['anonymous_user_contact']:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        global user
        user = User.query.filter_by(contact=form.contact.data).first()
        #session['anonymous_user_id'] = user.id
        session['anonymous_user_contact'] = form.contact.data
        if user:
            a = otp.generate_otp(int(form.contact.data))
            print(a, user.contact) 
            return redirect(url_for('otpverify'))
        else:
            flash(f'Phone number not registered, please sign up to register.', 'failure')
            return redirect(url_for('signup'))
    return render_template('login.html', form = form)

@app.route('/otp', methods=['GET', 'POST'])
@app.route('/otp.html', methods=['GET', 'POST'])
def otpverify():
    form = OtpForm()
    if form.validate_on_submit():
        if otp.verify_otp(form.otp.data):
            #login_user(user, remember=True)
            flash(f'Login successful!', 'success')
            #next_page = request.args.get('next')
            #return redirect(next_page) if next_page else redirect(url_for('index'))
            return redirect(url_for('index'))
        else:
            flash(f'Enter the correct otp', 'failure')
    return render_template('otpverify.html', form = form)

@app.route("/logout")
def logout():
    session['anonymous_user_contact'] = None
    return redirect(url_for('index'))


@app.route('/newpost', methods=['GET', 'POST'])
@app.route('/newpost.html', methods=['GET', 'POST'])
def newpost():
    if not session['anonymous_user_contact']:
        return redirect(url_for('login'))
    form = NewPostForm()
    if form.validate_on_submit():
        print('test1')
        print(session['anonymous_user_contact'])
        jobpost = JobPost(title=form.title.data, category=form.category.data, location=form.location.data, email=form.email.data, employer_contact=session['anonymous_user_contact'])
        print('test2')
        db.session.add(jobpost)
        print('test3')
        db.session.commit()
        print('test4')
        flash(f'Job posted', 'success')
        print('test5')
    return render_template('newpost.html', form = form)

@app.route('/jobpost', methods=['GET', 'POST'])
@app.route('/jobpost.html', methods=['GET', 'POST'])
def jobpost():
    a = JobPost.query.all()
    b = jobquery.convert(a)
    return render_template('jobpost.html', jobs = b)
