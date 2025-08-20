from typing import Optional, TypeVar
from pydantic import BaseModel, EmailStr
from datetime import date, datetime

T = TypeVar("T")

class BaseDTO(BaseModel):

    class Config:
        from_attributes = True


class RolUsuarioDTO(BaseDTO):
    id_rol: int
    rol: str


class UsuarioDTO(BaseDTO):
    email: EmailStr
    cedula: str
    nombres: str
    apellidos: str
    celular: str
    password_hash: str
    bool_status: bool
    created_at: datetime
    updated_at: Optional[date]
    deleted_at: Optional[date]
    id_rol: int


class RUsuarioDTO(UsuarioDTO):
    rol: RolUsuarioDTO


class UpdateUsuarioDTO(BaseDTO):
    email: str
    nombres: str
    apellidos: str

