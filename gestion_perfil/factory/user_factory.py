from datetime import datetime

from gestion_perfil.dto.user_rol_dto import UpdateUsuarioPasswordDTO
from gestion_perfil.models.user_model import UsuarioModel

from gestion_perfil.utils.managers import PasswordManager


class UserFactory:
    @staticmethod
    def update_user_from_update_dto(data:UpdateUsuarioPasswordDTO ) -> str:


        password_hash=PasswordManager.hash_password(data)
        return password_hash
    