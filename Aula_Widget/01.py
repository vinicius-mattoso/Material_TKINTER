######################################
# Teoria sobre widgets (componentes)
# Aula 02 das aulas da FEI de interface gráficas
# Vinicius Mattoso
######################################


#* Como utilizar o widget* 
# self.coisa = tk.NomeDoWidget (WidgetPai, opõesDeConfiguração)

######################################
# Widgets  na prática(componentes)
# Aula 03 das aulas da FEI de interface gráficas
# Vinicius Mattoso
######################################

import tkinter as tk
    

class Tela:
    def __init__(self, master):
        self.nossaTela = master

        #self.coisa = tk.NomeDoWidget (WidgetPai, opõesDeConfiguração)

        #! Criação de um texto ou imagem na tela #

        self.lbl = tk.Label(self.nossaTela, text= 'Olá mundo',  background= "red")

        self.lbl['font'] = ("Verdana" , "18")

        # metodo de posicionamento no tkinter
        # adquire os widgets junta em um bloco e joga na tela
        #OBS: quando usamos esse metodo, a tela fica resumida ao tamanho dos objetos
        self.lbl.pack()

        self.lbl2 = tk.Label(self.nossaTela, text= 'Esse é o meu segundo componente',  background= "blue")
        self.lbl2['font'] = ("Verdana" , "22")
        self.lbl2.pack()

        self.nossaTela.title("Segunda aula")

# Gerar a nossa interface
janelaRaiz = tk.Tk()

Tela(janelaRaiz)

janelaRaiz.mainloop()

