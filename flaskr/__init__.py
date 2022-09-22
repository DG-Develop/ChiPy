# import os
from flask import Flask
from flaskr.contratos.db.sql_server import get_db, init_db
from flaskr.cp_mexico.db.sql_server import get_db as db_cp_mexico, init_db as init_cp_mexico
from flaskr.contratos.routes.contrato_route import bp as bp_contrato
from flaskr.cp_mexico.routes.direcciones_route import bp as bp_cp_mexico

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']  = get_db()
app.config['SQLALCHEMY_BINDS']  = {
    'cp': db_cp_mexico()
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)
init_cp_mexico(app)

app.register_blueprint(bp_contrato)
app.register_blueprint(bp_cp_mexico)



# if __name__ == "__main__":
#     app.run(debug=True)

# from flaskr.db import get_db, init_db

# def create_app(test_config=None):
#     app = Flask(__name__, instance_relative_config=True)
    
#     # app.config.from_mapping(
#     #     SECRET_KEY='dev',
#     #     SQLALCHEMY_DATABASE_URI=get_db()
#     # )
#     app.config['SQLALCHEMY_DATABASE_URI'] = get_db()
    
#     # if test_config is None:
#     #     app.config.from_pyfile('config.py', silent=True)
#     # else:
#     #     app.config.from_mapping(test_config)
    
#     # try:
#     #     os.makedirs(app.instance_path)
#     # except OSError:
#     #     pass
    
#     @app.get("/")
#     def hello_world():
#         return "<h1>Hola Mundo</h1>"
    
#     # from . import db
#     # db.init_app(app)
#     init_db(app)
    
#     from . import contratos
#     app.register_blueprint(contratos.bp)
    
#     # # Remuevo la session una vez que la apliación se pare
#     # @app.teardown_appcontext
#     # def shutdown_session(exception=None):
#     #     print('Apagando...')
#     #     db_session.remove()
        
#     return app