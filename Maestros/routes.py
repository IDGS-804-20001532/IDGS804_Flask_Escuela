from flask import Blueprint, render_template, redirect, url_for, request, flash
from db import get_connection
from models import db
from models import Maestros
import forms

maestros= Blueprint('maestros', __name__)


@maestros.route("/insertarMaestro",methods=['GET', 'POST'])
def index():
    create_form=forms.MaestroForm(request.form)
    if request.method == 'POST':
        nombre=create_form.nombre.data,
        apaterno=create_form.apaterno.data,
        amaterno=create_form.amaterno.data,
        email=create_form.email.data,
        curp=create_form.curp.data,
        telefono=create_form.telefono.data

        try:
           connection=get_connection()
           with connection.cursor() as cursor:
                cursor.execute('call agregar_unMaestro(%s,%s,%s,%s,%s,%s)', (nombre, apaterno, amaterno, email, curp, telefono))
           connection.commit()
           connection.close()
           flash('Se inserto Correctamente!')

        except Exception as ex:
            print('ERROR {}'.format(ex))

        # Redirige al usuario a la vista ABCompleto
        return redirect(url_for('maestros.ABCompleto'))
    
    return render_template('guardarMaestros.html',form=create_form)
    

@maestros.route("/modificarMaestro",methods=['GET','POST'])
def modificar():
    create_fprm=forms.MaestroForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        connection = get_connection()
        try:
           with connection.cursor() as cursor:
               cursor.execute('CALL buscar_unMaestro(%s)',(id))
               resultset = cursor.fetchall()
               create_fprm.id.data=request.args.get('id')
               create_fprm.nombre.data=resultset[0][1]
               create_fprm.apaterno.data=resultset[0][2]
               create_fprm.amaterno.data=resultset[0][3]
               create_fprm.email.data=resultset[0][4]
               create_fprm.curp.data=resultset[0][5]  
               create_fprm.telefono.data=resultset[0][6]         
        except Exception as ex:
           print(ex)
        finally:
           connection.close()

    if request.method=='POST':
        id=create_fprm.id.data
        nombre=create_fprm.nombre.data,
        apaterno=create_fprm.apaterno.data,
        amaterno=create_fprm.amaterno.data,
        email=create_fprm.email.data,
        curp=create_fprm.curp.data,
        telefono=create_fprm.telefono.data
        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call modificar_unMaestro(%s,%s,%s,%s,%s,%s,%s)', (id, nombre, apaterno,amaterno, email, curp, telefono))
            connection.commit()
            connection.close()
            flash('El registro con nombre {} se modifico correctamente!'.format(nombre))

        except Exception as ex:
           print('ERROR {}'.format(ex))
        return redirect(url_for('maestros.ABCompleto'))
    return render_template('modificarMaestros.html', form= create_fprm)


@maestros.route("/eliminarMaestro",methods=['GET','POST'])
def eliminar():
    create_fprm=forms.MaestroForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        connection = get_connection()
        try:
           with connection.cursor() as cursor:
               cursor.execute('CALL buscar_unMaestro(%s)',(id))
               resultset = cursor.fetchall()
               create_fprm.id.data=request.args.get('id')
               create_fprm.nombre.data=resultset[0][1]
               create_fprm.apaterno.data=resultset[0][2]
               create_fprm.amaterno.data=resultset[0][3]
               create_fprm.email.data=resultset[0][4]
               create_fprm.curp.data=resultset[0][5]  
               create_fprm.telefono.data=resultset[0][6]         
        except Exception as ex:
           print(ex)
        finally:
           connection.close()
    if request.method=='POST':
        id=create_fprm.id.data
        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute('CALL eliminar_unMaestro(%s)', (id))
            connection.commit()
            connection.close()

        except Exception as ex:
           print('ERROR {}'.format(ex))
        return redirect(url_for('maestros.ABCompleto'))
    return render_template('eliminarMaestros.html', form= create_fprm)


@maestros.route("/ABCompletoMaestros",methods=["GET","POST"])
def ABCompleto():
    create_form=forms.MaestroForm(request.form)
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute('call buscar_Maestros()')
            resultset = cursor.fetchall()
            return render_template("ABCompletoMaestros.html", form=create_form, resultset=resultset)
    except Exception as ex:
        print(ex)
    finally:
        connection.close()
    return render_template("ABCompletoMaestros.html", form=create_form)
