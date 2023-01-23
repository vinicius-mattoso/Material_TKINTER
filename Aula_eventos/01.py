######################################
# Widgets  na prática(componentes)
# Aula 03 das aulas da FEI de interface gráficas
# Vinicius Mattoso
######################################

import tkinter as tk
from tkinter import messagebox
    

class Tela:
    def __init__(self, master):
        self.nossaTela = master

        self.lbl = tk.Label(self.nossaTela, text= 'Abrir caixa',  background= "green" , relief = "raised")
        self.lbl['font'] = ("Verdana" , "18")
        self.lbl.pack(pady = 20 )
        self.nossaTela.title("Aula de Eventos")
        #Button-1 -> botão esquerdo do mouse
        self.lbl.bind("<Button-1>", func = self.resposta_ao_click)

    def resposta_ao_click (seld, event):

        print(event.x , event.y)

        messagebox.showinfo(title = "Caixa de mensagem", message = ' Isso é uma mensagem')



# Gerar a nossa interface
janelaRaiz = tk.Tk()

Tela(janelaRaiz)

janelaRaiz.mainloop()