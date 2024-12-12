import orm.modelos as modelos
import orm.esquemas as esquemas
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

#post("/alumnos")
def guardar_alumno(sesion:Session, alu_nuevo:esquemas.AlumnoBase):
  
    alu_bd=modelos.alumnos()

    alu_bd.nombre=alu_nuevo.nombre
    alu_bd.edad=alu_nuevo.edad
    alu_bd.domicilio=alu_nuevo.domicilio
    alu_bd.carrera=alu_nuevo.carrera
    alu_bd.trimestre=alu_nuevo.trimestre
    alu_bd.email=alu_nuevo.email
    alu_bd.password=alu_nuevo.password
    
    sesion.add(alu_bd)
    sesion.commit()
    sesion.refresh(alu_bd)
    return alu_bd

#********Actualizar alumno*********
#put("/alumnos/{id}")
def actualizar_alumno(sesion:Session, id_al:int, alu_esquema:esquemas.AlumnoBase):
   
   alu_bd = alumno_por_id(sesion,id_al)
   if alu_bd is not None:
       alu_bd.nombre = alu_esquema.nombre
       alu_bd.edad = alu_esquema.edad
       alu_bd.domicilio = alu_esquema.domicilio
       alu_bd.carrera = alu_esquema.carrera
       alu_bd.trimestre = alu_esquema.trimestre
       alu_bd.email = alu_esquema.email
       alu_bd.password = alu_esquema.password

       sesion.commit()
       sesion.refresh(alu_bd)

       print(alu_esquema)
       return alu_esquema
   else:
       respuesta = {"No existe el alumno"}
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

#******Busca fotos por id del alumno*******
#Atiende a GET 'alumnos/{id}/fotos'
#select * from app.fotos WHERE id_alumnos={id_al}
def fotos_por_id_alumno(sesion:Session,id_al:int):
    print("select * from app.fotos where id_alumnos=", id_al)
    return sesion.query(modelos.fotos).filter(modelos.fotos.id_alumno==id_al).all() 

#***********Borra fotos por id*******
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
    fotos_al = fotos_por_id_alumno(sesion, id_al)
    if fotos_al is not None:
        for foto_alumno in fotos_al:
            sesion.delete(foto_alumno)
        sesion.commit()
        
#***********Guardar alumno************
#post("/alumnos/{id}/fotos")
def guardar_foto_por_id_alumno(sesion:Session, id_al:int,foto_nueva:esquemas.FotoBase):
   
    fo = fotos_por_id_alumno(sesion,id_al)

    if fo is not None:
        fo_bd = modelos.fotos()

        fo_bd.id_alumno = id_al
        fo_bd.titulo = foto_nueva.titulo
        fo_bd.descripcion = foto_nueva.descripcion
        fo_bd.ruta = foto_nueva.ruta
        sesion.add(fo_bd)
        sesion.commit()
        sesion.refresh(fo_bd)
        return fo_bd
    
#**********Actualizar foto*************
#put("/fotos/{id}")

def actualizar_foto(sesion:Session, id_fo:int, fo_esquema:esquemas.FotoBase):
   
   fo_bd = fotos_por_id(sesion,id_fo)
   if fo_bd is not None:
       fo_bd.titulo = fo_esquema.titulo
       fo_bd.descripcion = fo_esquema.descripcion
       fo_bd.ruta = fo_esquema.ruta

       sesion.commit()
       sesion.refresh(fo_bd)

       print(fo_esquema)
       return fo_esquema
   else:
       respuesta = {"No existe la foto"}
       return respuesta
#---------------Calificaciones--------------
#**********Busca calificaciones*************
#Atiende a GET 'calificaciones'
#select * from app.calificaciones
def devuelve_calificaciones(sesion:Session):
    print("select *from app.calificaciones")
    return sesion.query(modelos.calificaciones).all()

#**********Busca calificaciones por id********
#Atiende a GET 'calificaciones/{id}'
#select * from app.calificaciones WHERE id={id_fo}
def calificaciones_por_id(sesion:Session,id_ca:int):
    print("select * from app.calificaciones where id = ", id_ca)
    return sesion.query(modelos.calificaciones).filter(modelos.calificaciones.id==id_ca).first()

#*******Busca calificaciones por id del alumno******** 
#Atiende a GET 'alumnos/{id}/calificaciones'
#select * from app.calificaciones WHERE id_alumnos={id_al}
def calificaciones_por_id_alumno(sesion:Session,id_al:int):
    print("select * from app.calificaciones where id_alumnos=", id_al)
    return sesion.query(modelos.calificaciones).filter(modelos.calificaciones.id_alumno==id_al).all() 

#***********Elimina calificaciones por id*******
#*********DELETE '/calificaciones/{id}'***********
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

#post("/alumnos/{id}/calificaciones")
def guardar_calificacion_por_id_alumno(sesion:Session, id_al:int,foto_nueva:esquemas.FotoBase):
   
    ca = calificaciones_por_id_alumno(sesion,id_al)

    if ca is not None:
        ca_bd = modelos.calificaciones()

        ca_bd.id_alumno = id_al
        ca_bd.titulo = foto_nueva.titulo
        ca_bd.descripcion = foto_nueva.descripcion
        ca_bd.ruta = foto_nueva.ruta
        sesion.add(ca_bd)
        sesion.commit()
        sesion.refresh(ca_bd)
        return ca_bd
    
#*************Actualizar calificacion***************
#put("/calificaciones/{id}")
def actualizar_calificaciones(sesion:Session, id_ca:int, ca_esquema:esquemas.CalificaionBase):
   
   ca_bd = calificaciones_por_id(sesion,id_ca)
   if ca_bd is not None:
       ca_bd.uea = ca_esquema.uea
       ca_bd.calificacion = ca_esquema.calificacion

       sesion.commit()
       sesion.refresh(ca_bd)

       print(ca_esquema)
       return ca_esquema
   else:
       respuesta = {"No existe "}
       return respuesta