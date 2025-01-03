from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
import shutil
import os
import uuid
import orm.repo as repo 
import orm.esquemas as esquemas
from sqlalchemy.orm import Session
from orm.config import generador_sesion 

app = FastAPI()
#--------------Alumnos-----------------
#get("/alumnos”)
@app.get("/alumnos")
def lista_alumnos(sesion:Session=Depends(generador_sesion)):
    print("API consultando todos los alumnos")
    return repo.devuelve_alumnos(sesion)

#get("/alumnos/{id})
@app.get("/alumnos/{id}")
def alumno_por_id(id:int,sesion:Session=Depends(generador_sesion)):
    print("Api consultando alumno por id")
    return repo.alumno_por_id(sesion, id)

#delete("/alumnos/{id})
@app.delete("/alumnos/{id}")
def borrar_alumno(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borrar_calificaciones_por_id_usuario(sesion,id)
    repo.borrar_fotos_por_id_usuario(sesion,id)
    repo.borra_alumno_por_id(sesion,id)
    return {"Alumno eliminado"}

#post("/alumnos")
@app.post("/alumnos")
def guardar_alumnos(alumnos:esquemas.AlumnoBase, sesion:Session=Depends(generador_sesion)):
    print(alumnos)
    return repo.guardar_alumno(sesion,alumnos)

#put("/alumnos/{id}")
@app.put("/alumnos/{id}")
def actualizar_alumno(id:int, info_alumno:esquemas.AlumnoBase,sesion:Session=Depends(generador_sesion)):
    return repo.actualizar_alumno(sesion,id,info_alumno)
#----------------Fotos--------------------

#get("/fotos/{id}”)
@app.get("/fotos/{id}")
def fotos_por_id(id:int,sesion:Session=Depends(generador_sesion)):
    print("Api consultando fotos por id")
    return repo.fotos_por_id(sesion, id)

#get("/alumnos/{id}/fotos")
@app.get("alumnos/{id}/fotos")
def fotos_por_id_al(id:int,sesion:Session=Depends(generador_sesion)):
    print("API consultando fotos del alumno ", id)
    return repo.fotos_por_id_alumno(sesion, id)

#delete("/fotos/{id}”)
@app.delete("/fotos/{id}")
def borrar_foto(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borrar_fotos_por_id_usuario(sesion,id)
    return {"Foto eliminada"}

#delete("/alumnos/{id}/fotos")
@app.delete("/alumnos/{id}/fotos")
def borrar_foto_por_id(id:int, sesion: Session=Depends(generador_sesion)):
    repo.borrar_fotos_por_id_alumno(sesion, id)
    return {"Foto eliminada"}

#post("/alumnos/{id}/fotos")
@app.post("/alumnos/{id}/fotos")
def guardar_foto_por_id_alumno(id:int, fo: esquemas.FotoBase, sesion:Session=Depends(generador_sesion)):
    repo.guardar_foto_por_id_alumno(sesion, id, fo)

#put("/fotos/{id}")
@app.put("/fotos/{id}")
def actualizar_foto(id:int, info_foto:esquemas.FotoBase,sesion:Session=Depends(generador_sesion)):
    return repo.actualizar_foto(sesion,id,info_foto)

#---------------Calificaciones-------------
#get("/calificaciones/{id}”)
@app.get("/calificaciones/{id}")
def calificaciones_por_id(id:int,sesion:Session=Depends(generador_sesion)):
    print("Api consultando calificaciones por id")
    return repo.calificaciones_por_id(sesion, id)

#get("/alumnos/{id}/calificaciones")
@app.get("alumnos/{id}/calificaciones")
def calificaciones_por_id_al(id:int,sesion:Session=Depends(generador_sesion)):
    print("API consultando calificaciones del alumno ", id)
    return repo.calificaciones_por_id(sesion, id)

#delete("/calificaciones/{id}”)
@app.delete("/calificaciones/{id}")
def borrar_calificacion(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borrar_calificaciones_por_id_usuario(sesion,id)
    return {"Calificacion eliminada"}

#delete("/alumnos/{id}/calificaciones")
@app.delete("/alumnos/{id}/calificaciones")
def borrar_calificaciones_por_id(id:int, sesion: Session=Depends(generador_sesion)):
    repo.borrar_calificaciones_por_id_alumno(sesion, id)
    return {"Calificacion eliminada"}

#post("/alumnos/{id}/calificaciones")
def guardar_calificacion_por_id_alumno(id:int, ca: esquemas.CalificaionBase, sesion:Session=Depends(generador_sesion)):
    repo.guardar_calificacion_por_id_alumno(sesion, id, ca)

#put("/calificaciones/{id}")
@app.put("/calificaciones/{id}")
def actualizar_calificacion(id:int, info_cali:esquemas.CalificaionBase,sesion:Session=Depends(generador_sesion)):
    return repo.actualizar_calificaciones(sesion,id,info_cali)
