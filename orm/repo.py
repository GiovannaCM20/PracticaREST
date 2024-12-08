import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_

#----------------Alumnos-----------------
#*************Busca alumnos**************
#Atiende a GET 'alumnos'
#select * from, app.alumnos
def devuelve_alumnos(sesion:Session):
    print("select *from app.alumnos")
    return sesion.query(modelos.alumnos).all()

#***********Busca alumnos por id*********
#Atiende GET 'alumnos/{id}'
#select * from app.alumnos WHERE id={id_al}
def alumno_por_id(sesion:Session,id_al:int):
    print("select * from app.alumnos where id = ", id_al)
    return sesion.query(modelos.alumnos).filter(modelos.alumnos.id==id_al).first()

#***********Elimina alumnos por id*******
#DELETE '/alumnos/{id}'
#delete from app.alumnos WHERE id_alumnos={id_al}
def borra_alumno_por_id(sesion:Session,id_al:int):
    print("delete from app.alumnos where id_alumnos=", id_al)

    usr = alumno_por_id(sesion, id_al)
    #2.- Borramos
    if usr is not None:
        #Borramos usuario
        sesion.delete(usr)
        #Confirmar los cambios
        sesion.commit()
    respuesta = {
        "mensaje": "alumno eliminado"
    }
    return respuesta

#----------------Fotos-------------------
#**************Busca fotos***************
#Atiende a GET 'fotos'
#select * from app.fotos
def devuelve_fotos(sesion:Session):
    print("select *from app.fotos")
    return sesion.query(modelos.fotos).all()

#*************Busca fotos por id*********
#Atiende a GET 'fotos/{id}'
#select * from app.fotos WHERE id={id_fo}
def fotos_por_id(sesion:Session,id_fo:int):
    print("select * from app.fotos where id = ", id_fo)
    return sesion.query(modelos.fotos).filter(modelos.fotos.id==id_fo).first()

#Busca fotos por id del alumno 
#Atiende a GET 'alumnos/{id}/fotos'
#select * from app.fotos WHERE id_alumnos={id_al}
def fotos_por_id_alumno(sesion:Session,id_al:int):
    print("select * from app.fotos where id_alumnos=", id_al)
    return sesion.query(modelos.fotos).filter(modelos.fotos.id_alumno==id_al).all() 

#***********Elimina fotos por id*******
#DELETE '/fotos/{id}'
#delete from app.fotos WHERE id={id_fo}
def borra_fotos_por_id(sesion:Session,id_fo:int):
    print("delete from app.fotos where id=", id_fo)

    al = fotos_por_id(sesion, id_fo)
    #2.- Borramos
    if al is not None:
        #Borramos usuario
        sesion.delete(al)
        #Confirmar los cambios
        sesion.commit()
    respuesta = {
        "mensaje": "foto eliminada"
    }
    return respuesta

#*******Borra fotos por id del alumno*****
#DELETE '/alumnos/{id}/fotos'
#delete from app.fotos WHERE id_alumnos={id_al}
def borrar_fotos_por_id_alumno(sesion:Session,id_al:int):
    print("delete from app.calificaciones where id_alumno=",id_al)
    fotos_usr = fotos_por_id_alumno(sesion, id_al)
    if fotos_usr is not None:
        for foto_usuario in fotos_usr:
            sesion.delete(foto_usuario)
        sesion.commit()

#---------------Calificaciones--------------
#Busca calificaciones
#Atiende a GET 'calificaciones'
#select * from app.calificaciones
def devuelve_calificaciones(sesion:Session):
    print("select *from app.calificaciones")
    return sesion.query(modelos.calificaciones).all()

#Busca calificaciones por id
#Atiende a GET 'calificaciones/{id}'
#select * from app.calificaciones WHERE id={id_fo}
def calificaciones_por_id(sesion:Session,id_ca:int):
    print("select * from app.calificaciones where id = ", id_ca)
    return sesion.query(modelos.calificaciones).filter(modelos.calificaciones.id==id_ca).first()

#Busca calificaciones por id del alumno 
#Atiende a GET 'alumnos/{id}/calificaciones'
#select * from app.calificaciones WHERE id_alumnos={id_al}
def calificaciones_por_id_alumno(sesion:Session,id_al:int):
    print("select * from app.calificaciones where id_alumnos=", id_al)
    return sesion.query(modelos.calificaciones).filter(modelos.calificaciones.id_alumno==id_al).all() 

#***********Elimina calificaciones por id*******
#DELETE '/calificaciones/{id}'
#delete from app.calificaciones WHERE id={id_al}
def borra_calificacion_por_id(sesion:Session,id_al:int):
    print("delete from app.calificaciones where id=", id_al)

    usr = calificaciones_por_id(sesion, id_al)

    if usr is not None:
        sesion.delete(usr)
        sesion.commit()
    respuesta = {
        "mensaje": "Calificacion eliminada"
    }
    return respuesta

#******Borra calificaciones por id del alumno******
#DELETE '/alumnos/{id}/calificaciones'
#delete from app.calificaciones WHERE id_alumnos={id_al}
def borrar_calificaciones_por_id_alumno(sesion:Session,id_al:int):
    print("delete from app.fotos where id_alumnos=",id_al)
    calificaciones_usr = calificaciones_por_id_alumno(sesion, id_al)
    if calificaciones_usr is not None:
        for calificaciones_alumno in calificaciones_usr:
            sesion.delete(calificaciones_alumno)
        sesion.commit()