from sqlalchemy import Column, String, Boolean, Integer, CHAR, TIMESTAMP, ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


from datetime import date
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, String, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(AsyncAttrs, DeclarativeBase):
    pass


class RolUsuarioModel(Base):
    __tablename__ = "rol_usuario"

    id_rol: Mapped[int] = mapped_column(primary_key=True)
    rol: Mapped[str] = mapped_column(String(20), nullable=False)

    # Relación uno a muchos: un rol puede tener varios usuarios
    usuario: Mapped[List["UsuarioModel"]] = relationship(back_populates="rol")


class UsuarioModel(Base):
    __tablename__ = "usuario"

    email: Mapped[str] = mapped_column(String(100), primary_key=True)
    cedula: Mapped[str] = mapped_column(
        String(10), nullable=False)
    nombres: Mapped[str] = mapped_column(String(50), nullable=False)
    apellidos: Mapped[str] = mapped_column(String(50), nullable=False)
    celular: Mapped[str] = mapped_column(String(20), nullable=False)
    bool_status: Mapped[bool]
    created_at: Mapped[date] = mapped_column(Date, nullable=False)
    updated_at: Mapped[date] = mapped_column(Date, nullable=True)
    deleted_at: Mapped[date] = mapped_column(Date, nullable=True)

    id_rol: Mapped[int] = mapped_column(ForeignKey("rol_usuario.id_rol"))
    password_hash: Mapped[str] = mapped_column(String(200), nullable=False)
    rol: Mapped["RolUsuarioModel"] = relationship(back_populates="usuario")
""" class Base(AsyncAttrs, DeclarativeBase):
    pass

class Usuario (Base):
    __tablename__ = "usuario"

    cedula = Column(CHAR(10), primary_key=True, index=True)
    nombres = Column(String(50), nullable=False)
    apellidos = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    celular = Column(String(15), nullable=False)
    password_hash = Column(String(200), nullable=False)
    bool_status = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)
    id_rol = Column(Integer, ForeignKey("rol_usuario.id_rol")) """