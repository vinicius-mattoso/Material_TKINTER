######################################
# FRAMES
# Aula 09 das aulas da FEI de interface gráficas
# Vinicius Mattoso
######################################

#Frames são uma forma de widget, que funciona como um retangulo|container que serve para abrigar outros widgets dentro dele.

import tkinter as tk
    

class Tela:
    def __init__(self, master):
        self.nossaTela = master

        self.fr1 = tk.Frame(self.nossaTela)
        self.fr1.pack()
        self.fr2 = tk.Frame(self.nossaTela)
        self.fr2.pack(side=tk.BOTTOM)

        self.lbl = tk.Label(self.fr1, text= 'Esse é o meu primeiro componente',  background= "red")
        self.lbl['font'] = ("Verdana" , "18")
        self.lbl.pack(pady = 20, side = tk.LEFT, fill= tk.Y)

        self.lbl2 = tk.Label(self.fr2, text= 'Esse é o meu segundo componente',  background= "blue")
        self.lbl2['font'] = ("Verdana" , "22")
        self.lbl2.pack(ipadx = 25, ipady = 10, side = tk.LEFT)

        self.lbl3 = tk.Label(self.fr2, text= 'Esse é o meu terceiro componente',  background= "green")
        self.lbl3['font'] = ("Verdana" , "22")
        self.lbl3.pack(ipadx = 25, ipady = 10, side= tk.LEFT)

        self.nossaTela.title("Segunda aula")

# Gerar a nossa interface
janelaRaiz = tk.Tk()

Tela(janelaRaiz)

janelaRaiz.mainloop()