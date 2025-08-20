from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from gestion_perfil.dto.user_rol_dto import UsuarioDTO
from gestion_perfil.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, db: AsyncSession):
        self.repository = UserRepository(db)

    async def update_user(self, cedula: str, user) -> UsuarioDTO:
        result = await self.repository.update_user(cedula, user)
        if not result:
            return []
        result = UsuarioDTO.model_validate(result)
        return result
    
    async def update_user_password(self, cedula: str, new_password: str) -> UsuarioDTO:
        result = await self.repository.update_user_password(cedula, new_password)
        if not result:
            return []
        result = UsuarioDTO.model_validate(result)
        return result


