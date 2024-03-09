import sqlite3

conn = sqlite3.connect('empresa.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS empresas
             (nome TEXT, data_fundacao TEXT, num_funcionarios INTEGER, regiao_brasil TEXT, setor_atuacao TEXT)''')


def add_enterprise(empresa):
    c.execute("INSERT INTO empresas VALUES (?, ?, ?, ?, ?)",
              (empresa.nome, empresa.data_fundacao, empresa.num_funcionarios, empresa.regiao_brasil, empresa.setor_atuacao))
    conn.commit()

def delete_data():
    c.execute('DELETE FROM empresas')
    conn.commit()

def remove_duplicate():
    c.execute('''CREATE TABLE IF NOT EXISTS empresas_unicas AS
    SELECT DISTINCT * FROM empresas
    ''')
    conn.commit()
    c.execute('''DROP TABLE empresas''')
    conn.commit()
    c.execute('''ALTER TABLE empresas_unicas RENAME TO empresas''')
    conn.commit()
    
def check_if_table_exists(table_name):
    conn = sqlite3.connect("empresa.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    tabela = cursor.fetchone()

    conn.close()

    return tabela is not None

def drop_table():
    c.execute('''DROP TABLE empresas_importada''')
    conn.commit()