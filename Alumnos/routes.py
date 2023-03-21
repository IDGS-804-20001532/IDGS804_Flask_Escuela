from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import jsonify
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db
from models import Alumnos
import forms

alumnos= Blueprint('alumnos', __name__)


@alumnos.route("/insertar",methods=['GET', 'POST'])
def index():
    create_form=forms.UserForm(request.form)
    if request.method == 'POST':
        alum = Alumnos(matricula=create_form.matricula.data,
                    nombre=create_form.nombre.data,
                    apaterno=create_form.apaterno.data,
                    amaterno=create_form.amaterno.data,
                    email=create_form.email.data,
                    grupo=create_form.grupo.data)
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('alumnos.ABCompleto'))
    
    return render_template('index.html',form=create_form)

    

@alumnos.route("/modificar",methods=['GET','POST'])
def modificar():
    create_form=forms.UserForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        print('Esto es el id: ',id)
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=request.args.get('id')
        create_form.matricula.data=alum1.matricula
        create_form.nombre.data=alum1.nombre
        create_form.apaterno.data=alum1.apaterno
        create_form.amaterno.data=alum1.amaterno
        create_form.grupo.data=alum1.grupo
        create_form.email.data=alum1.email
    if request.method=='POST':
        id=create_form.id.data
        alum=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum.matricula=create_form.matricula.data
        alum.nombre=create_form.nombre.data
        alum.apaterno=create_form.apaterno.data
        alum.amaterno=create_form.amaterno.data
        alum.email=create_form.email.data
        alum.grupo=create_form.grupo.data
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('alumnos.ABCompleto'))
    return render_template('modificar.html', form= create_form)


@alumnos.route("/eliminar",methods=['GET','POST'])
def eliminar():
    create_form=forms.UserForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        print('Esto es el id: ',id)
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=request.args.get('id')
        create_form.matricula.data=alum1.matricula
        create_form.nombre.data=alum1.nombre
        create_form.apaterno.data=alum1.apaterno
        create_form.amaterno.data=alum1.amaterno
        create_form.grupo.data=alum1.grupo
        create_form.email.data=alum1.email
    if request.method=='POST':
        id=create_form.id.data
        alum=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('alumnos.ABCompleto'))
    return render_template('eliminar.html', form= create_form)


@alumnos.route("/ABCompleto",methods=["GET","POST"])
def ABCompleto():
    create_form=forms.UserForm(request.form)
    alumno=Alumnos.query.all()
    print(alumno)
    return render_template("ABCompleto.html",form=create_form,alumno=alumno)
