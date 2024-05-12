# refractory design pattern
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def create_app():
    app=Flask(__name__,template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite'
