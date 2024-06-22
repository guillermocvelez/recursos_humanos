from fastapi import APIRouter

#Importamos esta clase que nos permite definir respuestas HTTP
from fastapi.responses import  JSONResponse

#nos permite crear un esquema de datos
from pydantic import BaseModel
#una clase que nos permite colocar un atributo como opcional
from typing import List

from config.database import Session
from models.Pais import Pais as PaisModel

from fastapi.encoders import jsonable_encoder

pais_router = APIRouter()

class Pais(BaseModel):
  pais_id:int
  pais_nombre: str
  


@pais_router.get('/pais', tags=['paises'], response_model=List[Pais],status_code=200)
def get_countries():
  db = Session()
  result = db.query(PaisModel).all()
  return JSONResponse(status_code=201, content=jsonable_encoder(result))

@pais_router.get('/pais/{id}',tags=['paises'], response_model=Pais)
def get_country_by_id(id: int):
  db = Session()
  result = db.query(PaisModel).filter(PaisModel.pais_id == id).first()
  if not result:
    return JSONResponse(status_code=404, content={'mensaje': 'País no encontrado'})
  return JSONResponse(status_code=201, content=jsonable_encoder(result))


@pais_router.post('/pais', tags=['paises'], response_model=dict, status_code=201)
def create_country(country: Pais) -> dict:
  db = Session()
  new_country = PaisModel(**country.model_dump())
  db.add(new_country)
  db.commit()  
  return JSONResponse( status_code=201, content={"message": "Se ha registrado el pais correctamente"})  


@pais_router.put('/pais/{id}',tags=['paises'])
def update_country(id: int, country: Pais):

  db = Session()
  result = db.query(PaisModel).filter(PaisModel.pais_id == id).first()
  if not result:
    return JSONResponse(status_code=404, content={'mensaje': 'País no encontrado'})

  result.pais_nombre = country.pais_nombre
  db.commit()
  return JSONResponse(status_code=200, content={'mensaje': 'Se ha modificado el país'})


@pais_router.delete('/pais/{id}',tags=['paises'])
def delete_country(id: int):
  db = Session()
  result = db.query(PaisModel).filter(PaisModel.pais_id == id).first()
  if not result:
    return JSONResponse(status_code=404, content={'mensaje': 'País no encontrado'})
  
  db.delete(result)
  db.commit()

  return JSONResponse(status_code=200, content={'mensaje': 'Se ha eliminado el país'})