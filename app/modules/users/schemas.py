from pydantic import BaseModel, EmailStr, ConfigDict
from modules.users.models import UserRole

class UserBase(BaseModel):
    nome: str
    email: EmailStr 
    role: UserRole = UserRole.CLIENTE

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool

    # Configuração para permitir a criação a partir de objetos ORM (SQLAlchemy)
    model_config = ConfigDict(from_attributes=True)