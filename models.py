from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Albaran(db.Model):
    idAlbaran = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fechaRecepcion = db.Column(db.Date, nullable=False)
    proveedor = db.Column(db.String(100), nullable=False)
    productos = db.relationship('AlbaranProductos', backref='albaran', lazy=True)

class AlbaranProductos(db.Model):
    albaran_id = db.Column(db.Integer, db.ForeignKey('albaran.idAlbaran'), primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.idProducto'), primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)

class Productos(db.Model):
    idProducto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nameProduct = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=True)
    stock = db.Column(db.Integer, nullable=False)
    state = db.Column(db.Boolean, nullable=False)
    albaranes = db.relationship('AlbaranProductos', backref='productos', lazy=True)
    facturas = db.relationship('FacturasProductos', backref='productos', lazy=True)

class FacturasProductos(db.Model):
    idFactura = db.Column(db.Integer, db.ForeignKey('facturas.idFactura'), primary_key=True)
    idProducto = db.Column(db.Integer, db.ForeignKey('productos.idProducto'), primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)
    preu = db.Column(db.Numeric(10, 2), nullable=False)

class Facturas(db.Model):
    idFactura = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha = db.Column(db.Date, nullable=False)
    productos = db.relationship('FacturasProductos', backref='Facturas', lazy=True)