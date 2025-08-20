from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import get_session
from fastapi import APIRouter
from gestion_perfil.dto.general_dto import ResponseSchema
from gestion_perfil.dto.user_rol_dto import UpdateUsuarioDTO
from gestion_perfil.services.user_service import UserService


router = APIRouter()
@router.patch("/{cedula}", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_user(cedula: str, user_data: UpdateUsuarioDTO, db: AsyncSession = Depends(get_session)):
    """
    Update user information by cedula.
    """
    try:
        service = UserService(db)
        updated_user = await service.update_user(cedula, user_data)
        if not updated_user:
            return ResponseSchema(detail="User not found", result=None)
        return ResponseSchema(detail="User updated successfully", result=updated_user)
        return updated_user
    except Exception as e:
        return ResponseSchema(detail=f"An error occurred: {str(e)}", result=None)