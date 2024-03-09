import random
from datetime import datetime, timedelta
from faker import Faker

def random_date(): 
    year = random.randint(1900, 2022)
    day = random.randint(1, 365)
        
    return datetime(year, 1, 1) + timedelta(days=day - 1)

def company_name():
    fake = Faker()
    Faker.seed(random.randint(1,1000))

    return fake.company()

def number_of_employees():
    return random.randint(1,10000)

def region():
    return random.choice(['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul'])

def sector():
    return random.choice(['Industrial', 'Varejo', 'Serviços', 'Agrícola'])


