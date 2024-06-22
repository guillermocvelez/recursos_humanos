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

historico_router = APIRouter()