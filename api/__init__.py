from unicodedata import name
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sql

app = Flask(__name__)
CORS(app)

print('__name__ = ',__name__)

conn_str = (
    r'DRIVER={SQL Server};'
    r'SERVER=(local)\SKEATDEV;'
    r'DATABASE=Blog;'
    r'Trusted_Connection=yes;'
)

# Local postgres
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc://blogadmin:coolbeans@SKEATDEV/Blog?driver=SQL+Server"

#sqlite
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blog.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'My First API !!'