from flask import render_template,flash,redirect
from app import app
from .forms import LoginForm


@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                           title ='用户登录')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/socket.html')
def socket_index():
    return  render_template('socket.html')

@app.route('/sellers.html')
def seller_index():
    return render_template('sellers.html')