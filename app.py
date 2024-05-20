from flask import Flask
from routes import main
from models import db

#Creamos la app
app = Flask(__name__)

#Configuramos la app
app.config.from_object('config.DevConfig')

#Registramos las rutas
app.register_blueprint(main)

#Inicializamos el ORM
db.init_app(app)

#Creamos la base de datos
with app.app_context():
    db.create_all()