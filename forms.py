from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import EmailField
from wtforms import validators


class UserForm(Form):
    id=IntegerField('id',[validators.number_range(min=1, max=20, message='Valor no validado')])
    matricula=StringField('Matricula',[
        validators.DataRequired(message='Valor no valido')])
    nombre=StringField('Nombre',[
        validators.DataRequired(message='Valor no valido')])
    apaterno=StringField('Apellido Paterno',{
        validators.DataRequired(message='Valor no valido')})
    amaterno=StringField('Apellido Materno',{
        validators.DataRequired(message='Valor no valido')})
    email=EmailField('Correo',{
        validators.DataRequired(message='Valor no valido'),
        validators.Email(message='Ingresa un correo valido')})
    grupo=StringField('Grupo',[
        validators.DataRequired(message='Valor no valido')])

class MaestroForm(Form):
    id=IntegerField('id',[validators.number_range(min=1, max=20, message='Valor no validado')])
    nombre=StringField('Nombre',[
        validators.DataRequired(message='Valor no valido')])
    apaterno=StringField('Apellido Paterno',{
        validators.DataRequired(message='Valor no valido')})
    amaterno=StringField('Apellido Materno',{
        validators.DataRequired(message='Valor no valido')})
    email=EmailField('Correo',{
        validators.DataRequired(message='Valor no valido'),
        validators.Email(message='Ingresa un correo valido')})
    curp=StringField('CURP',[
        validators.DataRequired(message='Valor no valido')])
    telefono=StringField('Telefono',[
        validators.DataRequired(message='Valor no valido')])