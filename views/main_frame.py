import tkinter as tk
from tkinter import filedialog

class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        label = tk.Label(self, text='''  Bem vindo a aplicação! Com o inutito de resolver o teste técnico, foi criada essa aplicação.

  Clique no botão para ser encaminhado a página que realiza as consultas desejadas.''', 
                          font=("Helvetica", 10),width=100, anchor="center", wraplength=200, justify="left")
        label.pack(expand=True)

        button = tk.Button(self, text="Ir para querys", command=lambda: master.show_secondary_frame("Busca"))
        button.pack(side="bottom", padx=5, pady=5)

        import_button = tk.Button(self, text="Importar CSV", command=self.import_csv)
        import_button.pack(side="left", padx=5, pady=5)

        export_button = tk.Button(self, text="Exportar CSV", command=master.export_csv)
        export_button.pack(side="right", padx=5, pady=5)

    def import_csv(self):
        arquivo_csv = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if arquivo_csv:
            self.master.import_csv_insert(arquivo_csv)