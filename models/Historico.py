from config.database import Base
from sqlalchemy import Column,Sequence, Integer, String, ForeignKey, Float


HISTORICO_ID = Sequence('historico_id_sequence', start=1)

class Historico(Base):
  __tablename__ = "historico"

  emphist_id = Column(Integer, primary_key=True, server_default=HISTORICO_ID.next_value(), autoincrement=True)
  emphist_fecha_retiro = Column(String)
  empleado_id=Column(Integer)

