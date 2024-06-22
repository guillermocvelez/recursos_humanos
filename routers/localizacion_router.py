from fastapi import APIRouter

#Importamos esta clase que nos permite definir respuestas HTTP
from fastapi.responses import  JSONResponse

#nos permite crear un esquema de datos
from pydantic import BaseModel
#una clase que nos permite colocar un atributo como opcional
from typing import List

from config.database import Session
from models.Localizaciones import Localizacion as LocalizacionModel
from typing import Optional
from fastapi.encoders import jsonable_encoder

localizacion_router = APIRouter()

class Localizacion(BaseModel):
  localiz_id: Optional[int] = None
  localiz_direccion: str
  cuidad_id: Optional[int] = None

@localizacion_router.get('/localizacion', tags=['localizaciones'], response_model=List[Localizacion], status_code=200)
def get_localizaciones():
  db = Session()
  result = db.query(LocalizacionModel).all()
  return JSONResponse(status_code=202, content=jsonable_encoder(result))

@localizacion_router.get('/localizacion/{id}', tags=['localizaciones'], response_model=Localizacion,status_code=200)
def get_localizcion_by_id(id:int):
  db = Session()
  result = db.query(LocalizacionModel).filter(LocalizacionModel.localiz_id == id).first()
  if not result:
    return JSONResponse(status_code=404, content={'Mensaje': 'Localización no encontrada'})
  return JSONResponse(status_code=201, content=jsonable_encoder(result))
  


@localizacion_router.post('/localizacion', tags=['localizaciones'], response_model=dict, status_code=201)
def create_localizacion(localizacion: Localizacion):
  db = Session()
  new_localization = LocalizacionModel(**localizacion.model_dump())
  db.add(new_localization)
  db.commit()
  return JSONResponse(status_code=201, content={'mensaje': 'Se ha registrado la localización correctamente'})

@localizacion_router.put('/localizacion/{id}', tags=['localizaciones'])
def update_localizacion(id:int, localizacion: Localizacion):
  db = Session()
  result = db.query(LocalizacionModel).filter(LocalizacionModel.localiz_id == id).filter().first()
  print(result)
  if not result:
    JSONResponse(status_code=404, content={'mensaje': 'Locación no encontrada'})
  result.localiz_direccion = localizacion.localiz_direccion
  result.ciudad_id = localizacion.cuidad_id
  db.commit()
  return JSONResponse(status_code=200, content={'mensaje': 'Se ha modificado la loclaizacion'})


@localizacion_router.delete('/localizacion/{id}', tags=['paises'])
def delete_localizacion(id: int):
  db = Session()
  result = db.query(LocalizacionModel).filter(LocalizacionModel.localiz_id == id).first()
  if not result:
    JSONResponse(status_code=404, content={'mensaje': 'Locación no encontrada'})
  db.delete(result)
  db.commit()
  return JSONResponse(status_code=200, content={'mensaje': 'Localización eliminada'})
