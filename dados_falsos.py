
from fake_data.utils import random_date, company_name, number_of_employees, region, sector
from models.empresa import Empresa
from database.db_funtions import adicionar_empresa
import random

def create_fake_data():
    limit = random.randint(100,1000)
    for _ in range(limit):
        regiao_brasil = region()
        setor = sector()
        nome_empresa = company_name()
        data_fundacao = random_date()
        num_empregados = number_of_employees()
        new_empresa = Empresa(nome=nome_empresa, data_fundacao=data_fundacao, num_funcionarios=num_empregados, regiao_brasil=regiao_brasil, setor_atuacao=setor)
        adicionar_empresa(new_empresa)

create_fake_data()