from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Productos(db.Model):
    idProducto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nameProduct = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, nullable=False)

class AlbaranProductos(db.Model):
    albaran_id = db.Column(db.Integer, db.ForeignKey('albara.idAlbaran'), primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.idProducto'), primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)
    preu_unitat = db.Column(db.Numeric(10, 2), nullable=False)

class Albara(db.Model):
    idAlbaran = db.Column(db.Integer, primary_key=True)
    fechaRecepcion = db.Column(db.Date, nullable=False)
    proveedor = db.Column(db.String(100), nullable=False)