from datetime import datetime
from enum import Enum
from pydantic import BaseModel
from typing import Optional, TypeVar

T = TypeVar("T")


class BaseDTO(BaseModel):

    class Config:
        from_attributes = True


class LogDTO(BaseDTO):
    id_log: Optional[int]
    quien: str
    accion: str
    entidad_afectada: str
    fecha: datetime
    extra_data: str


class ResponseSchema(BaseDTO):
    detail: str
    result: Optional[T] = None


class Role(str, Enum):
    admin = "Admin"
    user = "User"


class Token(BaseDTO):
    access_token: str
    token_type: str


class TokenData(BaseDTO):
    email: str
    role: str
    id_usuario: Optional[int] = None
    nombe: Optional[str] = None