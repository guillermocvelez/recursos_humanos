from config.database import Base
from sqlalchemy import Column,Sequence, Integer, String, ForeignKey



CIUDAD_ID = Sequence('ciudad_id_sequence', start=1)

class Ciudad(Base):
  __tablename__ = "ciudades"

  ciud_id = Column(Integer, primary_key=True, server_default=CIUDAD_ID.next_value(),autoincrement=True)
  ciud_nombre = Column(String)
  pais_id = Column(Integer)