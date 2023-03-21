from flask_sqlalchemy import SQLAlchemy
import datetime


db =  SQLAlchemy()

class Alumnos(db.Model):
    __tablename__='alumnos'
    id=db.Column(db.Integer, primary_key=True)
    matricula=db.Column(db.String(10))
    nombre=db.Column(db.String(50))
    apaterno=db.Column(db.String(50))
    amaterno=db.Column(db.String(50))
    email=db.Column(db.String(50))
    grupo=db.Column(db.String(50))

class Maestros(db.Model):
    __tablename__='maestros'
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50))
    apaterno=db.Column(db.String(50))
    amaterno=db.Column(db.String(50))
    email=db.Column(db.String(50))
    curp=db.Column(db.String(18))
    telefono=db.Column(db.String(15))