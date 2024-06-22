from fastapi import APIRouter
from datetime import datetime

#Importamos esta clase que nos permite definir respuestas HTTP
from fastapi.responses import  JSONResponse

#nos permite crear un esquema de datos
from pydantic import BaseModel
#una clase que nos permite colocar un atributo como opcional
from typing import List

from config.database import Session
from models.Empleado import Empleado as EmpleadoModel
from models.Historico import Historico as HistoricoModel
from typing import Optional
from fastapi.encoders import jsonable_encoder

empleados_router = APIRouter()

class Empleado(BaseModel):
  empl_id: Optional[int] = None
  empl_primer_nombre: str
  empl_segundo_nombre: str
  empl_email: str
  empl_fecha_nac: str
  empl_sueldo: int
  empl_comision: float
  cargo_id: int
  departamento_id: int
  activo: bool

class Historico(BaseModel):
  emphist_fecha_retiro: str
  emphist_id: Optional[int] = None
  empleado_id: Optional[int] = None


@empleados_router.get('/empleados', tags=['empleados'])
def get_empleados():
  db = Session()
  result = db.query(EmpleadoModel).all()
  return JSONResponse(status_code=200,content=jsonable_encoder(result))


@empleados_router.get('/empleados/{id}', tags=['empleados'])
def get_empleado_by_id(id: int):
  db = Session()
  result = db.query(EmpleadoModel).filter(EmpleadoModel.empl_id == id).first()

  return JSONResponse(status_code=201, content=jsonable_encoder(result))


@empleados_router.post('/empleados', tags=['empleados'])
def create_empleado(empleado: Empleado):
  db = Session()
  new_empleado = EmpleadoModel(**empleado.model_dump())
  db.add(new_empleado)
  db.commit()
  return JSONResponse(status_code=201, content={'mensaje': 'Empleado creado correctamente'})


@empleados_router.put('/empleados/{id}',tags=['empleados'])
def update_empleado(id: int, empleado: Empleado):
  db = Session()
  result = db.query(EmpleadoModel).filter(EmpleadoModel.empl_id == id).first()
  if not result:
    return JSONResponse(status_code=404, content={'message':'Empleado no encontrado'})

  result.empl_primer_nombre = empleado.empl_primer_nombre
  result.empl_segundo_nombre = empleado.empl_segundo_nombre
  result.empl_sueldo = empleado.empl_sueldo
  result.empl_comision = empleado.empl_comision
  result.empl_email = empleado.empl_email
  result.empl_fecha_nac = empleado.empl_fecha_nac
  result.departamento_id = empleado.departamento_id
  result.cargo_id = empleado.cargo_id

  db.commit()

  return JSONResponse(status_code=200, content={'message':'Empleado Actualizado'})

@empleados_router.delete('/empleados/{id}', tags=['empleados'])
def delete_empleado(id: int):
  db = Session()
  result = db.query(EmpleadoModel).filter(EmpleadoModel.empl_id == id).first()
  if not result:
    return JSONResponse(status_code=404, content={'message':'Empleado no encontrado'})
  result.activo = False
  db.commit()
  new_historic = HistoricoModel(**{
    'emphist_fecha_retiro': datetime.now(),
    'empleado_id': id
  }) 

  db.add(new_historic)
  db.commit()

  return JSONResponse(status_code=200, content={'message':'Empleado Eliminado'})
  

  
