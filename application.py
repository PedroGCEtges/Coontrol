import sqlite3
import tkinter as tk
import csv
import re
from database.db_funtions import check_if_table_exists
from views.main_frame import MainFrame
from views.second_frame import SecondaryFrame
from views.first_query import FirstQuery
from utils import querys
from tkinter import filedialog, ttk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Minha Aplicação")
        self.geometry("400x300")
        self.current_frame = None

        self.database_connection = sqlite3.connect("empresa.db")
        self.cursor = self.database_connection.cursor()

        self.show_main_frame()

    def show_main_frame(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = MainFrame(self)
        self.current_frame.pack(expand=True, fill="both")

    def show_secondary_frame(self, action):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = SecondaryFrame(self, action=action)
        self.current_frame.pack(expand=True, fill="both")
    
    def show_query(self, action):
        self.show_results(action)
    
    def import_csv(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if filename:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.cursor.execute("INSERT INTO empresas (nome, data_fundacao, num_funcionarios, regiao_brasil, setor_atuacao ) VALUES (?, ?, ?, ?, ?)", row)
                self.database_connection.commit()

    def import_csv_insert(self, arquivo_csv):
        with open(arquivo_csv, 'r', newline='', encoding='latin-1') as arquivo:
            leitor_csv = csv.reader(arquivo)
            contador_linhas = 0
            self.cursor.execute("DROP TABLE IF EXISTS empresas_importado")
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS empresas_importada
             (nome TEXT, data_fundacao TEXT, num_funcionarios INTEGER, regiao_brasil TEXT, setor_atuacao TEXT)''')
            for linha in leitor_csv:
                self.cursor.execute("INSERT INTO empresas_importada (nome, data_fundacao, num_funcionarios, regiao_brasil, setor_atuacao ) VALUES (?, ?, ?, ?, ?)", linha)
                contador_linhas += 1
                if contador_linhas >= 10:
                    break
        self.database_connection.commit()

        self.mostrar_dados_importados()
    
    def mostrar_dados_importados(self):
        # Buscar as 10 primeiras linhas dos dados importados
        self.cursor.execute("SELECT * FROM empresas_importada LIMIT 10")
        dados_importados = self.cursor.fetchall()

        # Criar uma nova janela
        nova_janela = tk.Toplevel(self)
        nova_janela.title("Dados Importados")
        
        # Exibir uma mensagem de confirmação
        mensagem = tk.Label(nova_janela, text="Dados importados com sucesso!")
        mensagem.pack()

        # Criar uma tabela para exibir os dados importados
        tabela = ttk.Treeview(nova_janela, columns=("Nome", 
                                                    "Data de Fundação",
                                                    "Número de Funcionários", 
                                                    "Região do Brasil", 
                                                    "Setor"), show="headings")
        tabela.heading("Nome", text="Nome")
        tabela.heading("Data de Fundação", text="Data de Fundação")
        tabela.heading("Número de Funcionários", text="Número de Funcionários")
        tabela.heading("Região do Brasil", text="Região do Brasil")
        tabela.heading("Setor", text="Setor")
        for linha in dados_importados:
            tabela.insert("", "end", values=linha)
        tabela.pack(expand=True, fill="both")

    def export_csv(self):
        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if filename:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                self.cursor.execute("SELECT * FROM empresas")
                writer.writerows(self.cursor.fetchall())

    def show_results(self, action):
        if check_if_table_exists("empresas_importada"):
            queries = querys.set_table_to_query_at(table="empresas_importada")
            # print("ola"+queries)
        else:
            queries = querys.set_table_to_query_at()

        queries_mapping = {
            1: queries[0],
            2: queries[1],
            3: queries[2],
            4: queries[3],
            5: queries[4],
        }
        if action in queries_mapping:
            self.cursor.execute(queries_mapping[action])
        else:
            print("Erro")

        result = self.cursor.fetchall()

        nova_janela = tk.Toplevel(self)
        nova_janela.minsize(300,50)
        nova_janela.title("Resultado")
        
        mensagem = tk.Label(nova_janela, text=self.formatar_resultado(result, action))
        mensagem.pack()

    def formatar_resultado(self, result, action):
        if action == 1:
            1
        formatted_result = ""
        for row in result:
            formatted_result += " ".join(map(str, row)) + "\n"
        
        if action == 1:
            formatted_result = "Região: " + formatted_result.split(" ")[0] +'\n'+ "Nº Funcionários: " + formatted_result.split(" ")[1]

        if action == 2:
            formatted_result = "Empresa mais antiga: " +'\n' + formatted_result
        
        if action == 3:
            formatted_result = "Região: " + formatted_result.split(" ")[0] +'\n'+ "Nº de empresas no setor industrial: " + formatted_result.split(" ")[1]

        if action == 4:
            formatted_result = (formatted_result.split(" ")[0] + ": " + ''.join(re.findall(r'\d+',formatted_result.split(" ")[1])) + '\n' +
                                ''.join(re.findall(r'[a-zA-Zá-úÁ-Ú]+',formatted_result.split(" ")[1])) + ": " + ''.join(re.findall(r'\d+',formatted_result.split(" ")[2])) +'\n' +
                                ''.join(re.findall(r'[a-zA-Zá-úÁ-Ú]+',formatted_result.split(" ")[2])) + ": " + ''.join(re.findall(r'\d+',formatted_result.split(" ")[3])) +'\n' +
                                ''.join(re.findall(r'[a-zA-Zá-úÁ-Ú]+',formatted_result.split(" ")[3])) + ": " + formatted_result.split(" ")[4])
            
        if action == 5:
            formatted_result = "Nº total de funcionários de todas as empresas: " + formatted_result.split(" ")[0]
    
        return formatted_result