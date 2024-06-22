from fastapi import APIRouter

#Importamos esta clase que nos permite definir respuestas HTTP
from fastapi.responses import  JSONResponse

#nos permite crear un esquema de datos
from pydantic import BaseModel
#una clase que nos permite colocar un atributo como opcional
from typing import List

from config.database import Session
from models.Departamentos import Departamento as DepartamentoModel
from typing import Optional
from fastapi.encoders import jsonable_encoder

departamentos_router = APIRouter()

class Departamento(BaseModel):
  dpto_id: Optional[int] = None
  dpto_nombre: str
  localizacion_id: Optional[int] = None

@departamentos_router.get('/departamentos', tags=['departamentos'], response_model=List[Departamento], status_code=200)
def get_departamentos():
  db = Session()
  result = db.query(DepartamentoModel).all()
  return JSONResponse(status_code=200, content=jsonable_encoder(result))


@departamentos_router.get('/departamentos/{id}', tags=['departamentos'], response_model=Departamento)
def get_departament_by_id(id: int):
  db = Session()
  result = db.query(DepartamentoModel).filter(DepartamentoModel.dpto_id == id).first()
  return JSONResponse(status_code=201, content=jsonable_encoder(result))


@departamentos_router.post('/departamentos',tags=['departamentos'])
def create_departamento(departamento: Departamento):
  db = Session()
  new_departamento = DepartamentoModel(**departamento.model_dump())
  db.add(new_departamento)
  db.commit()
  return JSONResponse(status_code=201, content={'content': 'Departamento creado correctamente'})

@departamentos_router.put('/departamentos/{id}', tags=['departamentos'])
def update_departamento(id:int, departamento: Departamento):
  db = Session()
  result = db.query(DepartamentoModel).filter(DepartamentoModel.dpto_id == id).first()
  if not result:
    return JSONResponse(status_code=404, content={'mensaje': 'Departamento no encontrado'})
  
  result.dpto_nombre = departamento.dpto_nombre
  result.localizacion_id = departamento.localizacion_id
  db.commit()

  return JSONResponse(status_code=200, content={'mensaje':'Departamento actualizado correctamente'})

@departamentos_router.delete('/departamentos/{id}', tags=['departamentos'])
def delete_departamento(id: int):
  db = Session()
  result = db.query(DepartamentoModel).filter(DepartamentoModel.dpto_id == id).first()
  if not result:
    return JSONResponse(status_code=404, content={'mensaje': 'Departamento no encontrado'})
  
  db.delete(result)
  db.commit()

  return JSONResponse(status_code=200, content={'mensaje':'Departamento borrado correctamente'})


