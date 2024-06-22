from config.database import Base
from sqlalchemy import Column,Sequence, Integer, String, ForeignKey, Float, Boolean

EMPLEADO_ID = Sequence('empleado_id_sequence', start=1)

class Empleado(Base):
  __tablename__ = "empleados"

  empl_id = Column(Integer, primary_key=True, server_default=EMPLEADO_ID.next_value(), autoincrement=True)
  empl_primer_nombre = Column(String)
  empl_segundo_nombre = Column(String)
  empl_email = Column(String)
  empl_fecha_nac = Column(String)
  empl_sueldo = Column(Integer)
  empl_comision = Column(Float)
  cargo_id = Column(Integer)
  departamento_id= Column(Integer)
  activo= Column(Boolean)