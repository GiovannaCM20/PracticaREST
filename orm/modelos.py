from orm.config import BaseClass
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float
import datetime

class alumnos(BaseClass):
    id=Column(Integer, primary_key=True)
    nombre=Column(String(100))
    edad=Column(Integer)
    domicilio=Column(String(100))
    carrera=Column(String(100))
    trimestre=Column(String(100))
    email=Column("email", String(100))
    password=Column(String(100))
    fecha_registro=Column(DateTime(timezone=True),default=datetime.datetime.now)

class calificaciones(BaseClass):
    id=Column(Integer, primary_key=True)
    id_alumno=Column(Integer, ForeignKey(alumnos.id))
    uea=Column(String(100))
    calificacion=Column(String(100))

class fotos(BaseClass):
    id=Column(Integer, primary_key=True)
    id_alumno=Column(Integer, ForeignKey(alumnos.id))
    titulo=Column(String(100))
    descripcion=Column(String(100))
    ruta=Column(String(50))