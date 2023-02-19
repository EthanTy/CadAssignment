from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import pymysql

db = pymysql.connect(host='assignmentdatabase.co7landwei8p.us-east-1.rds.amazonaws.com',
                             port=3306,
                             user='admin',
                             password='Password',
                             database='lostfound'
                              )
                                   
# change db to rds database
# db = SQLAlchemy() host='assignmentdatabase.co7landwei8p.us-east-1.rds.amazonaws.com', port='3306' user='admin',password='password'
DB_NAME = "database.db"

sql_query = "select * from lostitem"
cursor = db.cursor()
cursor.execute(sql_query)
print("Total number of rows in table: ", cursor.rowcount)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ABCDEFU'

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # db.init_app(app)
    from .views import views

    # authententicationfor admin
    from .auth import auth

    # regular
    app.register_blueprint(views, url_prefix='/')
    # admin
    app.register_blueprint(auth, url_prefix='/')
    app.config['UPLOAD_FOLDER'] = 'static/uploads'
    app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif'}
    from.views import views

    return app
