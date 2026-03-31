# app/modules/users/services.py

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from modules.users.repositories import UserRepository
from modules.users.schemas import UserCreate
from core.security import get_password_hash 

class UserService:
    def __init__(self, db: Session):
        # O Serviço precisa do Repositório para falar com o banco
        self.repository = UserRepository(db)

    def create_user(self, user_in: UserCreate):
        existing_user = self.repository.get_by_email(user_in.email)
        
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Este email já está cadastrado no sistema."
            )
        user_in.password = get_password_hash(user_in.password)    
        
        return self.repository.create(user_in)

        # app/modules/users/services.py
from fastapi import HTTPException, status # Confirme se tem estes imports no topo!

class UserService:
    # ... (outras funções que já lá estão, como create_user) ...

    def delete_user(self, user_id: int):
        # Manda o repositório inativar o utilizador
        deleted_user = self.repository.delete(user_id)
        
        # Se o repositório devolver vazio (não encontrou o ID), lançamos erro 404
        if not deleted_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Utilizador não encontrado."
            )
        return deleted_user

