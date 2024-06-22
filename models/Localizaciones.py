from config.database import Base
from sqlalchemy import Column,Sequence, Integer, String, ForeignKey

LOCALIZACION_ID = Sequence('localizacion_id_sequence', start=1)

class Localizacion(Base):
  __tablename__ = "localizaciones"

  localiz_id = Column(Integer, primary_key=True, server_default=LOCALIZACION_ID.next_value() , autoincrement=True)
  localiz_direccion = Column(String)
  cuidad_id = Column(Integer, ForeignKey("ciudades.ciud_id"))