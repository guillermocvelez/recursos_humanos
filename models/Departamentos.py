from config.database import Base
from sqlalchemy import Column,Sequence, Integer, String, ForeignKey, Float

DEPARTAMENTO_ID = Sequence('departamento_id_sequence', start=1)

class Departamento(Base):
  __tablename__ = "departamentos"

  dpto_id = Column(Integer, primary_key=True, server_default=DEPARTAMENTO_ID.next_value(), autoincrement=True)
  dpto_nombre = Column(String)
  localizacion_id = Column(Integer)