import GPS as g
from tkinter import *
from tkinter import ttk as tk
from tkinter import messagebox

def pesquisar(inicio='', fim=''):
    g.grafo.resetar_cidades()
    inicio_vertice = None
    fim_vertice = None
    caminho.config(text="Caminho: ")

    if inicio == '' or fim == '':
        messagebox.showinfo("Escolha suas localizações", "Por favor, escolha suas localizações.")
        return 0

    for estacao in g.grafo.lista_estacao:
        if estacao.rotulo == inicio:
            inicio_vertice = estacao
        if estacao.rotulo == fim:
            fim_vertice = estacao

    objetivo = g.Gulosa(fim_vertice)
    objetivo.buscar(inicio_vertice)
    estacoes = objetivo.retonar_estacoes()

    if estacoes != False:
        for estacao in estacoes:
            texto = caminho.cget("text") + " --> " + estacao
            caminho.config(text=texto)
    else:
        texto = "Impossivel encontrar o destino final com a Busca Gulosa."
        caminho.config(text=texto)

#Inicialização da Tela
janela = Tk()
janela.title("Minha Interface")
janela.resizable(False, False)

#Configuração do Grid
janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=3)

#titulo
titulo = tk.Label(janela, text="GPS - Trens em Romênia", font=('Arial', 13))
titulo.grid(column=1, row=0, padx=5, pady=5)

# Label Inicial
label_Inicial = tk.Label(janela, text="Local Inicial")
label_Inicial.grid(column=0, row=1, padx=0, pady=0)

#Combobox Incio
caixa_inicio = tk.Combobox(janela, textvariable="bruh", state="readonly")
caixa_inicio['values'] = ('Arad', 'Zerind', 'Oradea', 'Sibiu', 'Timisoara', 'Lugoj', 'Mehadia', 'Dobreta', 'Craiova', 'Rimnicu', 'Fagaras', 'Pitesti', 'Bucharest', 'Giurgiu', 'Urziceni', 'Hirsova', 'Eforie', 'Vaslui', 'Iasi', 'Neamt')
caixa_inicio.grid(column=0, row=2, padx=10, pady=10)

# Destino Final
destino = tk.Label(janela, text="Destino Final")
destino.grid(column=2, row=1, padx=10, pady=10)

#Combobox Destino
caixa_final = tk.Combobox(janela, textvariable="burh", state="readonly")
caixa_final['values'] = ('Arad', 'Zerind', 'Oradea', 'Sibiu', 'Timisoara', 'Lugoj', 'Mehadia', 'Dobreta', 'Craiova', 'Rimnicu', 'Fagaras', 'Pitesti', 'Bucharest', 'Giurgiu', 'Urziceni', 'Hirsova', 'Eforie', 'Vaslui', 'Iasi', 'Neamt')
caixa_final.grid(column=2, row=2, padx=10, pady=10)

#Botão
botao = tk.Button(janela, text="Calcular Rota", command=lambda: pesquisar(caixa_inicio.get(), caixa_final.get()))
botao.grid(column=1, row=3, padx=5, pady=5)

#caminho
caminho = tk.Label(janela, text="Caminho: ", font=('Arial', 8))
caminho.grid(column=0, columnspan=3,row=4, padx=10, pady=10)

canvas = Canvas(bg="lightgray", highlightbackground="black", highlightthickness=3, height=300, width=560)
canvas.grid(column=0, row=5,columnspan=3)

#Estações
E_arad   = canvas.create_rectangle(20, 105, 30, 115, fill="grey")
L_arad = canvas.create_text(40, 125, text="Arad", fill="black", font=('Arial', 8))
E_zerind = canvas.create_rectangle(40, 70, 50, 80, fill="grey")
L_zerind = canvas.create_text(55, 90, text="Zerind", fill="black", font=('Arial', 8))
E_oradea = canvas.create_rectangle(60, 35, 70, 45, fill="grey")
L_oradea = canvas.create_text(40, 40, text="Oradea", fill="black", font=('Arial', 8))
E_timisoara = canvas.create_rectangle(25, 165, 35, 175, fill="grey")
L_timisoara = canvas.create_text(60, 165, text="Timisoara", fill="black", font=('Arial', 8))
E_sibiu = canvas.create_rectangle(120, 125, 130, 135, fill="grey")
L_sibiu = canvas.create_text(120, 145, text="Sibiu", fill="black", font=('Arial', 8))
E_lugoj = canvas.create_rectangle(80, 185, 90, 195, fill="grey")
L_lugoj = canvas.create_text(105, 190, text="Lugoj", fill="black", font=('Arial', 8))
E_mehadia = canvas.create_rectangle(85, 225, 95, 235, fill="grey")
L_mehadia = canvas.create_text(117, 230, text="Mehadia", fill="black", font=('Arial', 8))
E_dobreta = canvas.create_rectangle(80, 260, 90, 270, fill="grey")
L_dobreta = canvas.create_text(85, 276, text="Dobreta", fill="black", font=('Arial', 8))
E_rimnicu = canvas.create_rectangle(150, 175, 160, 185, fill="grey")
L_rimnicu = canvas.create_text(180, 175, text="Rimnicu", fill="black", font=('Arial', 8))
E_craiova = canvas.create_rectangle(160, 265, 170, 275, fill="grey")
L_craiova = canvas.create_text(190, 270, text="Craiova", fill="black", font=('Arial', 8))
E_fagaras = canvas.create_rectangle(195, 130, 205, 140, fill="grey")
L_fagaras = canvas.create_text(200, 120, text="Fagaras", fill="black", font=('Arial', 8))
E_pitesti = canvas.create_rectangle(205, 205, 215, 215, fill="grey")
L_pitesti = canvas.create_text(207, 225, text="Pitesti", fill="black", font=('Arial', 8))
E_bucareste = canvas.create_rectangle(255, 235, 265, 245, fill="grey")
L_bucareste = canvas.create_text(296, 245, text="Bucareste", fill="black", font=('Arial Black', 8))
E_giurgiu = canvas.create_rectangle(235, 275, 245, 285, fill="grey")
L_giurgiu = canvas.create_text(265, 280, text="Giurgiu", fill="black", font=('Arial', 8))
E_urziceni = canvas.create_rectangle(315, 215, 325, 225, fill="grey")
L_urziceni = canvas.create_text(293, 215, text="Urziceni", fill="black", font=('Arial', 8))
E_hirsova = canvas.create_rectangle(395, 215, 405, 225, fill="grey")
L_hirsova = canvas.create_text(425, 220, text="Hirsova", fill="black", font=('Arial', 8))
E_eforie = canvas.create_rectangle(435, 255, 445, 265, fill="grey")
L_eforie = canvas.create_text(442, 275, text="Eforie", fill="black", font=('Arial', 8))
E_vaslui = canvas.create_rectangle(375, 130, 385, 140, fill="grey")
L_vaslui = canvas.create_text(402, 135, text="Vaslui", fill="black", font=('Arial', 8))
E_iasi = canvas.create_rectangle(325, 80, 335, 90, fill="grey")
L_iasi = canvas.create_text(345, 85, text="Isai", fill="black", font=('Arial', 8))
E_neamt = canvas.create_rectangle(265, 55, 275, 65, fill="grey")
L_neamt = canvas.create_text(270, 47, text="Neamt", fill="black", font=('Arial', 8))

#Linhas
L_arad_zerind = canvas.create_line(25, 105, 40, 80, width=2)
L_zerind_oradea = canvas.create_line(45, 70, 60, 45, width=2)
L_oradea_sibiu = canvas.create_line(70, 45, 120, 125, width=2)
L_arad_sibiu = canvas.create_line(30, 107, 120, 130, width=2)
L_arad_timisoara = canvas.create_line(22, 115, 27, 165, width=2)
L_timisoara_lugoj = canvas.create_line(35, 172, 80, 188, width=2)
L_lugoj_mehadia = canvas.create_line(82, 195, 88, 225, width=2)
L_mehadia_dobreta = canvas.create_line(88, 235, 82, 260, width=2)
L_sibiu_romnicu = canvas.create_line(128, 135, 153, 175, width=2)
L_sibiu_fagaras = canvas.create_line(130, 132, 195, 135, width=2)
L_dobreta_craiova = canvas.create_line(90, 268, 160, 267, width=2)
L_rimnicu_craiova = canvas.create_line(158, 185, 162, 265, width=2)
L_rimnicu_pitesti = canvas.create_line(160, 182, 205, 207, width=2)
L_fagaras_bucareste = canvas.create_line(205, 140, 258, 235, width=2)
L_pitesti_bucareste = canvas.create_line(215, 210, 255, 235, width=2)
L_bucareste_giurgiu = canvas.create_line(260, 245, 245, 275, width=2)
L_bucareste_urziceni = canvas.create_line(265, 238, 315, 222, width=2)
L_urziceni_hirsova = canvas.create_line(325, 220, 395, 220, width=2)
L_urziceni_vaslui = canvas.create_line(322, 215, 378, 140, width=2)
L_hirsova_eforie = canvas.create_line(402, 225, 438, 255, width=2)
L_vaslui_iasi = canvas.create_line(379, 130, 332, 90, width=2)
L_iasi_neamt = canvas.create_line(325, 83, 275, 62, width=2)

janela.geometry("600x600")
janela.mainloop()