from flask import Flask
from app.database import criar_tabela
from app.routes import api

def criar_app():
    app = Flask(__name__)

    criar_tabela()
    app.register_blueprint(api)

    return app