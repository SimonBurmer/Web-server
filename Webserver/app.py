from flask import Flask, redirect, url_for, render_template, request, session, flash 
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)

    #register views
    from views import *

    #Database config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://b2ce470d26edb7:3a20aa4d@eu-cdbr-west-03.cleardb.net/heroku_9e47351aae0ada8'
    db = SQLAlchemy(app) 

    app.secret_key ="uiusdakasfkjfasd4389078532turieahfg87z5021gkjdha43178dsiugqkjh15478" #you have to look over it again
    app.permanent_session_lifetime = timedelta(minutes = 5) #defines how long things are saved in the session
    
    return app