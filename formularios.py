from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DecimalField
from wtforms.validators import DataRequired

class AlbaranForm(FlaskForm):
    producto0 = StringField('Producto 0', validators=[DataRequired()])
    cantidad0 = IntegerField('Cantidad 0', validators=[DataRequired()])
    producto1 = StringField('Producto 1', validators=[DataRequired()])
    cantidad1 = IntegerField('Cantidad 1', validators=[DataRequired()])
    producto2 = StringField('Producto 2', validators=[DataRequired()])
    cantidad2 = IntegerField('Cantidad 2', validators=[DataRequired()])
    producto3 = StringField('Producto 3', validators=[DataRequired()])
    cantidad3 = IntegerField('Cantidad 3', validators=[DataRequired()])
    producto4 = StringField('Producto 4', validators=[DataRequired()])
    cantidad4 = IntegerField('Cantidad 4', validators=[DataRequired()])
    proveedor = StringField('Proveedor', validators=[DataRequired()])
    submit = SubmitField('Enviar')

class FacturasForm(FlaskForm):
    producto0 = StringField('Producto 0', validators=[DataRequired()])
    cantidad0 = IntegerField('Cantidad 0', validators=[DataRequired()])
    producto1 = StringField('Producto 1', validators=[DataRequired()])
    cantidad1 = IntegerField('Cantidad 1', validators=[DataRequired()])
    producto2 = StringField('Producto 2', validators=[DataRequired()])
    cantidad2 = IntegerField('Cantidad 2', validators=[DataRequired()])
    producto3 = StringField('Producto 3', validators=[DataRequired()])
    cantidad3 = IntegerField('Cantidad 3', validators=[DataRequired()])
    producto4 = StringField('Producto 4', validators=[DataRequired()])
    cantidad4 = IntegerField('Cantidad 4', validators=[DataRequired()])
    submit = SubmitField('Enviar')

class UpdatePriceForm(FlaskForm):
    price = DecimalField('Precio', validators=[DataRequired()])
    submit = SubmitField('Guardar')