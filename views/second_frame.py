import tkinter as tk

class SecondaryFrame(tk.Frame):
    def __init__(self, master, action):
        super().__init__(master)
        self.action = action

        self.columnconfigure(0, weight=1, minsize=60)
        self.columnconfigure(1,weight=2, minsize=200)

        button_actions = [
            ("Busca 1", lambda: master.show_query(1),'''Apresenta o nome da região do brasil que apresenta maior número de funcionários e o nº de funcionários'''),
            ("Busca 2", lambda: master.show_query(2), '''Apresenta o nome da empresa mais antiga'''),
            ("Busca 3", lambda: master.show_query(3), "Apresenta a região do brasil que tem maior número de empresas do setor Industrial"),
            ("Busca 4", lambda: master.show_query(4), "Apresenta o número de empresas de cada setor de atuação em ordem decrescente"),
            ("Busca 5", lambda: master.show_query(5), "Apresenta o número total de funcionários de todas as empresas")
        ]

        for i, (action, action_command, description) in enumerate(button_actions):
            button = tk.Button(self, text=action, command=action_command, height=2)
            button.grid(row=i, column=0, padx=60, pady=10, sticky="nsew")  
            # self.grid_columnconfigure(0, weight=1)  

            label = tk.Label(self, text=description, wraplength=200, justify="left")
            label.grid(row=i, column=1, padx=1, pady=5, sticky="w")
        
        back_button = tk.Button(self, text="Voltar", command=master.show_main_frame)
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
