from flask import render_template,flash,redirect
from app import app
from .forms import LoginForm


@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title ='用户登录', form = form)