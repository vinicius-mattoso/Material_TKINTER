######################################
# Posicionamento dos Widgets
# Aula 04 das aulas da FEI de interface gráficas
# Vinicius Mattoso
######################################



#########################################
#                                       #
#   padx & pady -> margens externas     #
#                                       #
#                                       #
#   ipadx & ipady -> margens internas   #
#                                       #
#   side -> posicionamento de ancoragem #
#                                       #
#   fill -> orientação para onde vamos  #
#               expandir o componente   #
#                                       #
#########################################

import tkinter as tk
    

class Tela:
    def __init__(self, master):
        self.nossaTela = master

        self.lbl = tk.Label(self.nossaTela, text= 'Esse é o meu primeiro componente',  background= "red")
        self.lbl['font'] = ("Verdana" , "18")
        self.lbl.pack(pady = 20, side = tk.LEFT, fill= tk.Y)

        self.lbl2 = tk.Label(self.nossaTela, text= 'Esse é o meu segundo componente',  background= "blue")
        self.lbl2['font'] = ("Verdana" , "22")
        self.lbl2.pack(ipadx = 25, ipady = 10, side = tk.RIGHT)

        self.lbl3 = tk.Label(self.nossaTela, text= 'Esse é o meu terceiro componente',  background= "green")
        self.lbl3['font'] = ("Verdana" , "22")
        self.lbl3.pack(ipadx = 25, ipady = 10, fill= tk.X)

        self.nossaTela.title("Segunda aula")

# Gerar a nossa interface
janelaRaiz = tk.Tk()

Tela(janelaRaiz)

janelaRaiz.mainloop()

