from fastapi import FastAPI
from config.database import engine,Base
from routers.pais_router import pais_router
from routers.ciudad_router import ciudad_router
from routers.localizacion_router import localizacion_router
from routers.cargos_router import cargos_router
from routers.departamentos_router import departamentos_router
from routers.empleados_router import empleados_router

#Creamos una instancia de FastApi - FastApi es el framework que vamos a usar
app = FastAPI()

app.include_router(pais_router)
app.include_router(ciudad_router)
app.include_router(localizacion_router)
app.include_router(cargos_router)
app.include_router(empleados_router)
app.include_router(departamentos_router)

Base.metadata.create_all(bind=engine)





#





