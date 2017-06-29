from flask import render_template,flash,redirect
from app import app
from .forms import UploadForm
from flask import request


@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html',user = app.config['USERS'])


@app.route('/index.html')
def index():
    upload = UploadForm()
    return render_template('index.html')


@app.route('/socket.html')
def socket_index():
    return  render_template('socket.html')

@app.route('/sellers.html')
def seller_index():
    return render_template('sellers.html')