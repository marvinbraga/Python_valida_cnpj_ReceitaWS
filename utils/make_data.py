import pandas as pd
from faker import Faker

# Inicializar o gerador de dados fictícios
fake = Faker()

# Criar dados fictícios para contratantes
data = {
    "CNPJ": [fake.unique.random_number(digits=14, fix_len=True) for _ in range(10)],
    "Nome da Empresa": [fake.company() for _ in range(10)],
    "Endereço": [fake.address() for _ in range(10)],
    "Telefone": [fake.phone_number() for _ in range(10)],
    "E-mail": [fake.email() for _ in range(10)],
    "Setor": [fake.job() for _ in range(10)],
    "Data de Fundação": [fake.date_between(start_date='-30y', end_date='today') for _ in range(10)]
}

# Criar DataFrame com os dados
df = pd.DataFrame(data)

# Salvar o DataFrame como um arquivo Excel
file_path = '../.res/contratantes.xlsx'
df.to_excel(file_path, index=False)
