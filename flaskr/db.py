from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from flask import g


def get_db():
    if 'db' not in g:
        server = "172.19.2.31"
        database = "Contratos"
        user = "gdavid"
        pwd = "David2021"

        cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + \
            server + ';DATABASE=' + database + ';UID=' + user + ';PWD=' + pwd
            
        connection_url = URL.create(
            "mssql+pyodbc", query={"odbc_connect": cstr})
        
        engine=create_engine(connection_url)
        g.db=engine

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    get_db()
