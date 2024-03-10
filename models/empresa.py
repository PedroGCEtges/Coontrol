from datetime import datetime
from pydantic import BaseModel, Field

class Empresa(BaseModel):
    nome: str = Field(...)
    data_fundacao: datetime
    num_funcionarios:  int
    regiao_brasil: str = Field(...)
    setor_atuacao: str = Field(...)