from datetime import datetime
from typing import Optional, Literal
from pydantic import BaseModel, Field, validator

class Empresa(BaseModel):
    nome: str = Field(...)
    data_fundacao: datetime
    num_funcionarios:  int
    regiao_brasil: str = Field(...)
    setor_atuacao: str = Field(...)