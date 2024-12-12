from pydantic import BaseModel

#Definir el esquema alumno
class AlumnoBase(BaseModel):
    nombre:str
    edad:int
    domicilio:str
    carrera:str
    trimestre:str
    email:str
    password:str

#Definir el esquema calificaciones
class CalificaionBase(BaseModel):
    uea:str
    calificacion:str
    
#Definir el esquema fotos
class FotoBase(BaseModel):
    titulo:str
    descripcion:str 
    ruta:str