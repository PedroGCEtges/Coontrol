import tkinter as tk

class FirstQuery(tk.Frame):
    def __init__(self, master, query):
        super().__init__(master)

        self.query = query

        self.result_label = tk.Label(self, text="Resultado:")
        self.result_label.pack()

        result = self.fetch_result()
        self.result_text = tk.Text(self, height=10, width=50)
        self.result_text.insert(tk.END, result)
        self.result_text.pack()

    def fetch_result(self):
        self.master.cursor.execute(self.query)
        result = self.master.cursor.fetchone()
        if result:
            return result[0]
        else:
            return "Nenhum resultado encontrado."