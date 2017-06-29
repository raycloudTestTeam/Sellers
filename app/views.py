from flask import render_template,flash,redirect,url_for
from app import app
from app.usually_tools.get_all_coin import *
from flask import request


@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html',user = app.config['USERS'])


@app.route('/index.html')
def index():
    #icon = ALLCOIN()
    # result = icon.get_all_coin()
    return render_template('index.html')

@app.route('/get_icon',methods=['POST'])
def get_icon():
    form = request.form
    test = form.get("test")
    if not test:
        flash("please input test")
        return render_template("index.html")
    if test ==u"test":
        flash("test success")
        return render_template("index.html")
    else:
        flash("test error")
        return render_template("index.html")

@app.route('/socket.html')
def socket_index():
    return  render_template('socket.html')

@app.route('/sellers.html')
def seller_index():
    return render_template('sellers.html')