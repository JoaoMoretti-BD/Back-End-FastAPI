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
    """
    Serviço para gestão de regras de negócio de Utilizadores.
    
    Centraliza a lógica de validação, verificação de duplicidade e coordenação
    entre as operações de banco de dados.
    """

    def __init__(self, db: Session):
        """
        Inicializa o serviço com a sessão de banco de dados.
        
        Instancia o repositório de utilizadores necessário para acesso aos dados.
        
        Args:
            db (Session): Sessão ativa do SQLAlchemy.
        """
        self.repository = UserRepository(db)

    def create_user(self, user_in: UserCreate):
        """
        Cria um novo utilizador aplicando as regras de negócio.

        Verifica se o email já está cadastrado antes de permitir a criação.
        Caso o email já exista, interrompe o fluxo com um erro HTTP 400.

        Args:
            user_in (UserCreate): Dados do utilizador a ser criado.

        Returns:
            User: O utilizador criado e persistido.

        Raises:
            HTTPException: Se o email já estiver em uso (Status 400).
        """
        # Regra de Negócio 1: Verificar unicidade do email
        existing_user = self.repository.get_by_email(user_in.email)
        
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Este email já está cadastrado no sistema."
            )
        
        # Se a validação passou, delega a persistência ao repositório
        return self.repository.create(user_in)