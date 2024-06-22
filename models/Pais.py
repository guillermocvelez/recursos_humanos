from config.database import Base
from sqlalchemy import Column,Sequence, Integer, String

PAIS_ID = Sequence('pais_id_sequence', start=1)

class Pais(Base):
  __tablename__ = "paises"

  pais_id = Column(Integer, primary_key=True, server_default=PAIS_ID.next_value(),autoincrement=True)
  pais_nombre = Column(String)


