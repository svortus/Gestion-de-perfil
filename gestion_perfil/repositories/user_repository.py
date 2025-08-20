from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from typing import List, Optional
from gestion_perfil.models import user_model, rol_user_model

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    

    async def update_user(self,cedula: str, user: user_model.UsuarioModel) -> Optional[user_model.UsuarioModel]:
        result = await self.db.execute(
            select(user_model.UsuarioModel)
            .where(user_model.UsuarioModel.cedula == cedula)
        )
        data = result.scalars().first()
        if not data:
            return None
        data.email = user.email
        data.nombres = user.nombres
        data.apellidos = user.apellidos
        await self.db.commit()
        await self.db.refresh(data)
        return data
    
    async def update_user_password(self, cedula: str, new_password: str) -> Optional[user_model.UsuarioModel]:
        result = await self.db.execute(
            select(user_model.UsuarioModel)
            .where(user_model.UsuarioModel.cedula == cedula)
        )
        user = result.scalars().first()
        if not user:
            return None
        user.password_hash = new_password
        await self.db.commit()
        await self.db.refresh(user)
        return user
    