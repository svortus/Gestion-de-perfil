from sqlalchemy import Column, String, Boolean, Integer, CHAR, TIMESTAMP, ForeignKey
from config.database import Base


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
    id_rol = Column(Integer, ForeignKey("rol_usuario.id_rol"))