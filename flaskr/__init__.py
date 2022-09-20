import os
from flask import Flask
from flaskr.db import get_db, init_db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     SQLALCHEMY_DATABASE_URI=get_db()
    # )
    app.config['SQLALCHEMY_DATABASE_URI'] = get_db()
    
    # if test_config is None:
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     app.config.from_mapping(test_config)
    
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass
    
    @app.get("/")
    def hello_world():
        return "<h1>Hola Mundo</h1>"
    
    # from . import db
    # db.init_app(app)
    init_db(app)
    
    from . import contratos
    app.register_blueprint(contratos.bp)
    
    # # Remuevo la session una vez que la apliación se pare
    # @app.teardown_appcontext
    # def shutdown_session(exception=None):
    #     print('Apagando...')
    #     db_session.remove()
        
    return app