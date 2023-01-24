######################################
# Entrada de dados
# Aula 07 das aulas da FEI de interface gráficas
# Vinicius Mattoso
######################################

# O tradicional input que utilizamos em python vai ser o novo Entry.

# input -> CLI console Application
# entry -> GUI Graphical Application

# OBS: O formato tradicional de entrada e o string

# var = input()

# self.entrada = tk.Entry (WidgetPai, opõesDeConfiguração)
# self.qualquer = float( self.entrada.get() )

# não podemos utilizar a opção de height para controlar a altura da entrada, pois a mesma vai ser sempre de uma linha!

#bonus:
# a opção show='*' dentro do .Entry, faz com que tudo que o usuário digitar fique escondido por *

import tkinter as tk


class Tela:
    def __init__(self, master):

        self.nossaTela = master

        #adicionando um texto a nossa interface
        self.texto1 = tk.Label(self.nossaTela, text="Por gentilize,\n insira seu nome:")
        self.texto1.pack(side=tk.LEFT, fill=tk.X)

        #adicionando um widget de entrada de dados
        self.entrada = tk.Entry(self.nossaTela)
        self.entrada.pack(side=tk.LEFT, padx=10)

        #adicionando um widget de botão já pronto para servir como aceite do nome 
        self.btn = tk.Button(self.nossaTela, text="Confirmar",bg='green', command=self.mostraNome)
        self.btn.pack(side=tk.LEFT, padx=10)

    def mostraNome(self):
        self.nome = self.entrada.get()
        print('Olá:' + self.nome + " seja muito bem vindo a minha primeira interface")

janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()