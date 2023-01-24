######################################
# O widget Button
# Aula 08 das aulas da FEI de interface gráficas
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
        self.lbl.bind("<Button-1>", func = self.click)
        self.lbl.bind("<ButtonRelease>", func = self.resposta_ao_click)

        #fazendo o processo do botão de maneira mais apropriada e intuitiva
        self.btn = tk.Button(self.nossaTela, text="Clique aqui!", background= "red", command=self.respostabtn)
        self.btn['font'] = ("Verdana" , "18")
        self.btn.pack()
    
    def respostabtn(self):
        messagebox.showinfo(title = "Caixa de mensagem", message = ' Isso é uma mensagem')



    def click (self, event):
        print(event.x , event.y)
        # quando clicar no botão vamos mudar sua coloração
        self.lbl['relief'] = "sunken"

    def resposta_ao_click (self, event):
        #apenas quando soltarmos o botão do click que vamos executar uma função
        print(event.x , event.y)
        self.lbl['relief'] = "raised"

        messagebox.showinfo(title = "Caixa de mensagem", message = ' Isso é uma mensagem')



# Gerar a nossa interface
janelaRaiz = tk.Tk()

Tela(janelaRaiz)

janelaRaiz.mainloop()