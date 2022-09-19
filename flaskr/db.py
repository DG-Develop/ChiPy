from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def get_db():
    
    server = "172.19.2.31"
    database = "Contratos"
    user = "gdavid"
    pwd = "David2021"

    cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + \
        server + ';DATABASE=' + database + ';UID=' + user + ';PWD=' + pwd
        
    connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": cstr})
        
        # engine=create_engine(connection_url)
        # g.db=engine
        
    return connection_url
# g.db=engine

# db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
# Base = declarative_base()
# Base.query = db_session.query_property()


# def close_db(e=None):
#     db = g.pop('db', None)

#     if db is not None:
#         db.close()


def init_db(app):
    # import flaskr.models
    # Base.metadata.create_all(bind=engine)
    db.init_app(app)
