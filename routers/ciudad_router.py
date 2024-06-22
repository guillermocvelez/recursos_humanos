from fastapi import APIRouter

#Importamos esta clase que nos permite definir respuestas HTTP
from fastapi.responses import  JSONResponse

#nos permite crear un esquema de datos
from pydantic import BaseModel
#una clase que nos permite colocar un atributo como opcional
from typing import List

from config.database import Session
from models.Ciudad import Ciudad as CiudadModel
from typing import Optional
from fastapi.encoders import jsonable_encoder

ciudad_router = APIRouter()

class Ciudad(BaseModel):
  ciud_id: Optional[int] = None
  ciud_nombre:str
  pais_id: Optional[int] = None


@ciudad_router.get('/ciudad', tags=['ciudades'], response_model=List[Ciudad],status_code=200)
def get_ciudades():
  db = Session()
  result = db.query(CiudadModel).all()
  return JSONResponse(status_code=201, content=jsonable_encoder(result))

@ciudad_router.get('/ciudad/{id}', tags=['paises'], response_model=Ciudad,status_code=200)
def get_city_by_id(id: int):
  db = Session()
  result = db.query(CiudadModel).filter(CiudadModel.ciud_id == id).first()
  if not result:
    return JSONResponse(status_code=404, content={'Mensaje': 'Ciudad no encontrada'})
  return JSONResponse(status_code=201, content=jsonable_encoder(result))

@ciudad_router.post('/ciudad', tags=['ciudades'], response_model=dict, status_code=201)
def create_country(city: Ciudad) -> dict:
  db = Session()
  new_city = CiudadModel(**city.model_dump())
  db.add(new_city)
  db.commit()  
  return JSONResponse( status_code=201, content={"message": "Se ha registrado la ciudad correctamente"})  


@ciudad_router.put('/ciudad/{id}', tags=['ciudades'])
def update_ciudad(id: int, city: Ciudad):
  db = Session()
  result = db.query(CiudadModel).filter(CiudadModel.ciud_id == id).first()
  if not result:
    JSONResponse(status_code=404, content={'mensaje': 'ciudad no encontrada'})
  result.ciud_nombre = city.ciud_nombre
  db.commit()

  return JSONResponse(status_code=200, content={'mensaje': 'Se ha modificado la ciudad'})

@ciudad_router.delete('/ciudad/{id}', tags=['paises'])
def delete_city(id: int):
  db = Session()
  result = db.query(CiudadModel).filter(CiudadModel.ciud_id == id).first()
  if not result:
    return JSONResponse(status_code=404, content={'mensaje': 'ciudad no encontrada'})
  
  db.delete(result)
  db.commit()
  return JSONResponse(status_code=200, content={'mensaje': 'ciudad eliminada'})

