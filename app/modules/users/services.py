"""
Módulo de Serviços (Business Logic) de Utilizadores.

Este módulo contém a camada de serviços, responsável por implementar as regras de negócio
da aplicação. Ele atua como um intermediário entre o controlador (Router) e a camada de
dados (Repository), garantindo que validações e lógica complexa sejam executadas antes
da persistência.
"""

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from modules.users.repositories import UserRepository
from modules.users.schemas import UserCreate

class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def create_user(self, user_in: UserCreate):
        # Regra de Negócio 1: Verificar unicidade do email
        existing_user = self.repository.get_by_email(user_in.email)
        
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Este email já está cadastrado no sistema."
            )
        
        # Se a validação passou, delega a persistência ao repositório
        return self.repository.create(user_in)
