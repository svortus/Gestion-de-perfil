from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase

class Base(AsyncAttrs, DeclarativeBase):
    pass

class RolUsuario(Base):
    __tablename__ = "rol_usuario"

    id_rol = Column(Integer, primary_key=True, index=True)
    rol = Column(String(20), nullable=False)



