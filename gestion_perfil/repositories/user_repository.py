from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from typing import List, Optional
from gestion_perfil.models import usuario_model, rol_user_model

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    

    async def update_user(cedula: int, self, user: usuario_model.Usuario) -> usuario_model.Usuario:
        result = await self.db.execute(
            select(usuario_model.Usuario)
            .options(selectinload(usuario_model.Usuario))  # carga relación
            .where(usuario_model.Usuario.cedula == cedula)
        )
        data = result.scalars().first()
        if not data:
            return None
        data.email = user.email
        data.nombres = user.nombres
        await self.db.commit()
        await self.db.refresh(data)
        return data
    
    async def update_user_password(self, cedula: str, new_password: str) -> Optional[usuario_model.Usuario]:
        result = await self.db.execute(
            select(usuario_model.Usuario)
            .where(usuario_model.Usuario.cedula == cedula)
        )
        user = result.scalars().first()
        if not user:
            return None
        user.password_hash = new_password
        await self.db.commit()
        await self.db.refresh(user)
        return user
    