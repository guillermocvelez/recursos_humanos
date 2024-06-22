from fastapi import APIRouter

#Importamos esta clase que nos permite definir respuestas HTTP
from fastapi.responses import  JSONResponse

#nos permite crear un esquema de datos
from pydantic import BaseModel
#una clase que nos permite colocar un atributo como opcional
from typing import List

from config.database import Session
from models.Cargo import Cargo as CargoModel
from typing import Optional
from fastapi.encoders import jsonable_encoder

cargos_router = APIRouter()

class Cargos(BaseModel):
  cargo_id: Optional[int] = None
  cargo_nombre: str
  cargo_sueldo_minimo:str
  cargo_suedlo_maximo:str

@cargos_router.get('/cargos', tags=['cargos'],response_model=List[Cargos], status_code=200)
def get_cargos():
  db = Session()
  result = db.query(CargoModel).all()
  return JSONResponse(status_code=200, content=jsonable_encoder(result))


@cargos_router.get('/cargos/{id}', tags=['localizaciones'], response_model=Cargos,status_code=200)
def get_cargo_by_id(id: int):
  db = Session()
  result = db.query(CargoModel).filter(CargoModel.cargo_id == id).first()

  if not result:
    return JSONResponse(status_code=404, content={'mensaje': 'Cargo no encontrado'})
  
  return JSONResponse(status_code=201, content=jsonable_encoder(result))

@cargos_router.post('/cargos', tags=['cargos'],response_model=Cargos, status_code=201)
def create_cargo(cargo: Cargos):
  db = Session()
  new_cargo = CargoModel(**cargo.model_dump())
  db.add(new_cargo)
  db.commit()
  return JSONResponse(status_code=201, content={'mensaje': 'Se ha registrado el cargo correctamente'})

@cargos_router.put('/cargos/{id}',tags=['cargos'])
def update_cargo(id: int, cargo: Cargos):
  db = Session()
  result = db.query(CargoModel).filter(CargoModel.cargo_id == id).first()
  if not result:
    return JSONResponse(status_code=404, content={'mensaje': 'Cargo no encontrado'})
  
  result.cargo_nombre = cargo.cargo_nombre
  result.cargo_sueldo_minimo = cargo.cargo_sueldo_minimo
  result.cargo_suedlo_maximo = cargo.cargo_suedlo_maximo
  db.commit()
  return JSONResponse(status_code=201, content={'mensaje': 'Se ha actualizado el cargo correctamente'})

@cargos_router.delete('/cargos/{id}', tags=['cargos'])
def delete_cargo(id: int):
  db = Session()
  result = db.query(CargoModel).filter(CargoModel.cargo_id == id).first()
  if not result:
    return JSONResponse(status_code=404, content={'mensaje': 'Cargo no encontrado'})
  
  db.delete(result)
  db.commit()

  return JSONResponse(status_code=201, content={'mensaje': 'Se ha borrado el cargo correctamente'})

