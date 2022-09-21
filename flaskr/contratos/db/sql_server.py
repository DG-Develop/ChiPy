from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.engine import URL

db=SQLAlchemy()
ma = Marshmallow()

def get_db():
    
    server = "172.19.2.31"
    database = "Contratos"
    user = "gdavid"
    pwd = "David2021"

    cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + \
        server + ';DATABASE=' + database + ';UID=' + user + ';PWD=' + pwd
        
    connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": cstr})
    return connection_url

def init_db(app):
    db.init_app(app)
    ma.init_app(app)
