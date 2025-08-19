from sqlalchemy import Column, Integer, String
from config.database import Base  # Asegúrate de tener bien importado esto


class RolUsuario(Base):
    __tablename__ = "rol_usuario"

    id_rol = Column(Integer, primary_key=True, index=True)
    rol = Column(String(20), nullable=False)



