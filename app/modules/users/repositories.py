"""
Módulo de Repositório de Utilizadores.

Este módulo implementa o padrão Repository para abstrair a camada de acesso a dados.
Ele centraliza as operações de consulta e persistência relacionadas à entidade 'User',
mantendo o código de acesso ao banco separado das regras de negócio.
"""

from sqlalchemy.orm import Session
from modules.users.models import User
from modules.users.schemas import UserCreate

class UserRepository:
    """
    Repositório para manipulação de dados de Utilizadores.

    Gerencia as operações de CRUD (Create, Read, Update, Delete) para a tabela de utilizadores.
    """

    def __init__(self, db: Session):
        """
        Inicializa o repositório com uma sessão de banco de dados.

        Args:
            db (Session): Sessão ativa do SQLAlchemy para interação com o banco.
        """
        self.db = db

    def get_by_email(self, email: str):
        """
        Busca um utilizador pelo endereço de email.

        Args:
            email (str): Email a ser pesquisado.

        Returns:
            User | None: O objeto User se encontrado, ou None caso contrário.
        """
        return self.db.query(User).filter(User.email == email).first()

    def create(self, user_in: UserCreate):
        """
        Cria um novo utilizador no banco de dados.

        Args:
            user_in (UserCreate): Dados de entrada validados para criação do utilizador.

        Returns:
            User: O objeto User recém-criado e atualizado com o ID do banco.
        """
        # Converte o Schema para o Modelo de BD
        # NOTA DIDÁTICA: A senha é salva diretamente por enquanto. Será hash na próxima etapa de segurança.
        db_user = User(
            nome=user_in.nome,
            email=user_in.email,
            hashed_password=user_in.password,
            role=user_in.role
        )
        
        # Adiciona o novo usuário à sessão do banco de dados para ser persistido
        self.db.add(db_user)
        # Confirma as mudanças no banco de dados, executando a inserção
        self.db.commit()
        # Atualiza o objeto db_user com os dados do banco (como o ID gerado automaticamente)
        self.db.refresh(db_user)
        # Retorna o usuário recém-criado
        return db_user