from flask import Flask
from routes import main
from models import db
from flask_wtf.csrf import CSRFProtect

#Creamos la app
app = Flask(__name__)
csrf = CSRFProtect(app)

app.config['SECRET_KEY'] = 'una-clave-secreta-muy-segura'

#Configuramos la app
app.config.from_object('config.DevConfig')

#Registramos las rutas
app.register_blueprint(main)

#Inicializamos el ORM
db.init_app(app)

#Creamos la base de datos
with app.app_context():
    db.create_all()