from flask import Blueprint, flash, render_template, redirect, url_for, request
from models import Productos, Albaran, Facturas, db, AlbaranProductos, FacturasProductos
from formularios import AlbaranForm, FacturasForm
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/productos')
def productos():
    productos = Productos.query.all()
    return render_template('productos.html', productos=productos)

@main.route('/producto/<int:idProducto>', methods=['GET'])
def producto(idProducto):
    producto = Productos.query.get_or_404(idProducto)
    return render_template('producto.html', producto=producto)

@main.route('/ver-mas/<int:idProducto>', methods=['GET'])
def ver_mas(idProducto):
    return redirect(url_for('main.producto', idProducto=idProducto))

@main.route('/albaranes', methods=['GET', 'POST'])
def albaran():
    form = AlbaranForm()
    if request.method == 'POST' and form.validate_on_submit():
        albaran = Albaran()
        albaran.fechaRecepcion = datetime.now()
        albaran.proveedor = form.proveedor.data  # Obtener el proveedor del formulario

        db.session.add(albaran)
        db.session.commit()

        for i in range(5):  # Iterar sobre los 5 productos
            producto_nombre = request.form.get(f'producto{i}')
            cantidad = request.form.get(f'cantidad{i}', type=int)

            if producto_nombre and cantidad:
                producto = Productos.query.filter_by(nameProduct=producto_nombre).first()
                if producto:
                    producto.stock += cantidad
                    db.session.commit()

                    albaran_producto = AlbaranProductos(albaran_id=albaran.idAlbaran, producto_id=producto.idProducto, cantidad=cantidad)
                    db.session.add(albaran_producto)
                else:
                    new_product = Productos(nameProduct=producto_nombre, stock=cantidad, price=None, state=True)
                    db.session.add(new_product)
                    db.session.commit()

                    albaran_producto = AlbaranProductos(albaran_id=albaran.idAlbaran, producto_id=new_product.idProducto, cantidad=cantidad)
                    db.session.add(albaran_producto)
        db.session.commit()

        print('Albarán creado con éxito y guardado en la base de datos!')
        return redirect(url_for('main.productos'))

    return render_template('albaran.html', form=form)

@main.route('/facturas', methods=['GET', 'POST'])
def facturas():
    form = FacturasForm()
    if request.method == 'POST' and form.validate_on_submit():
        factura = Facturas()
        factura.fecha = datetime.now()
        db.session.add(factura)
        db.session.commit()
        for i in range(5):
            productoInput = request.form.get(f'producto{i}')
            cantidadInput = request.form.get(f'cantidad{i}', type=int)
            producto = Productos.query.filter_by(nameProduct=productoInput).first()
            if producto:
                if producto.stock >= cantidadInput and producto.state == True:
                    producto.stock -= cantidadInput
                    db.session.commit()
                    factura_producto = FacturasProductos(idFactura=factura.idFactura, idProducto=producto.idProducto, cantidad=cantidadInput, preu=producto.price)
                    db.session.add(factura_producto)
                else:
                    print('No hay suficiente stock de', productoInput)
                    flash(f'El producto {productoInput} no existe', 'error')
            else:
                print('El producto', productoInput, 'no existe')
                # Aquí lanzamos el mensaje de error
                flash(f'El producto {productoInput} no existe', 'error')
        return redirect(request.url)
    else:
        print("Error en el formulario.")
    return render_template("facturas.html", form=form)
@main.route('/update_price/<int:idProducto>', methods=['POST'])
def update_price(idProducto):
    producto = Productos.query.get_or_404(idProducto)
    if request.method == 'POST':
        nuevo_precio = request.form.get('price')
        if nuevo_precio:
            producto.price = nuevo_precio
            db.session.commit()
            return redirect(url_for('main.producto', idProducto=idProducto))
    return redirect(url_for('main.producto', idProducto=idProducto))

@main.route('/toggle_state/<int:idProducto>', methods=['POST'])
def toggle_state(idProducto):
    producto = Productos.query.get_or_404(idProducto)
    producto.state = not producto.state
    db.session.commit()
    flash(f'El estado del producto {producto.nameProduct} ha sido actualizado.', 'success')
    return redirect(url_for('main.producto', idProducto=idProducto))

