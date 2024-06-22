from config.database import Base
from sqlalchemy import Column,Sequence, Integer, String, ForeignKey

CARGO_ID = Sequence('cargo_id_sequence', start=1)

class Cargo(Base):
  __tablename__ = "cargos"

  cargo_id = Column(Integer, primary_key=True, server_default=CARGO_ID.next_value(), autoincrement=True)
  cargo_nombre = Column(String)
  cargo_sueldo_minimo = Column(String)
  cargo_suedlo_maximo = Column(String)