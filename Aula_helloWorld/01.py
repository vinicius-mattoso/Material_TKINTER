import tkinter as tk
    

class Tela:
    def __init__(self, master):
        self.nossaTela = master
        self.nossaTela.title("Primeira aula")

# Gerar a nossa interface
janelaRaiz = tk.Tk()

Tela(janelaRaiz)

janelaRaiz.mainloop()

