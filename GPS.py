import numpy as np

class Vertice:    
  def __init__(self, rotulo):
    self.rotulo = rotulo   
    self.visitado = False 
    self.adjacentes = []

  def adiciona_adjacente(self, adjacente):   
    self.adjacentes.append(adjacente)

  def retorna_adjacente(self):
    return self.adjacentes

class Adjacente:
  def __init__(self, vertice, custo):
    self.vertice = vertice
    self.custo = custo

# Classe que junta as duas classes (vértice e adjacente - Grafo completo)
class Grafo:
  # Cadastro das cidades
  lista_estacao = []
  linha = []
  linha_atual = 0
  
  cidades = open('cidades.txt', 'r')
  for i in range(0, 20):
    lista_estacao.append(Vertice(cidades.readline().replace("\n", '')))
  cidades.close()

  adjacentes = open('adjacentes.txt', 'r', encoding="utf-8")
  linha = adjacentes.readlines()

  j = 0
  while j != len(linha):

    if linha[j][:1].isupper():
      j += 1
      linha_atual += 1 

    if linha[j][:1].islower or linha[i].isalnum:
      cidade = linha[j].replace("\n", '')
      indice_cidade = 0
      for indice_cidade in range(0, len(lista_estacao)):
        if cidade == lista_estacao[indice_cidade].rotulo.lower():
          break
      j += 1
      custo = int(linha[j].replace("\n", ''))
      lista_estacao[linha_atual-1].adiciona_adjacente(Adjacente(lista_estacao[indice_cidade], custo))

    j += 1
  
  adjacentes.close()

  def resetar_cidades(self):
    for i in range(0, 18):
      self.lista_estacao[i].visitado = False


grafo = Grafo() 

# Classe que ordena os valores pelo custo (distancia)
class VetorOrdenado:

  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    # Mudança no tipo de dados
    self.valores = np.empty(self.capacidade, dtype=object)

  # Referência para o vértice e comparação com a distância para o objetivo
  def insere(self, vertice):

    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade máxima atingida')
      return
    posicao = 0

    for i in range(self.ultima_posicao + 1):
      sair_loop = False
      posicao = i
      j = 0

      for j in range(0, len(self.valores[i].adjacentes)):
        for k in range(0, len(vertice.adjacentes)):
          if self.valores[i].adjacentes[0].custo > vertice.adjacentes[k].custo and vertice.adjacentes[k].vertice.rotulo == self.valores[i].adjacentes[j].vertice.rotulo:
            sair_loop = True
            break
        if sair_loop:
          break

      if sair_loop:
        break
      if i == self.ultima_posicao:
        posicao = i + 1

    x = self.ultima_posicao
    while x >= posicao:
      self.valores[x + 1] = self.valores[x]
      x -= 1

    self.valores[posicao] = vertice
    self.ultima_posicao += 1

  def imprime(self, atual):
    if self.ultima_posicao == -1:
      print('O vetor está vazio')
    else:
      for i in range(self.ultima_posicao + 1):
        for j in range(len(self.valores[i].adjacentes)):
          if self.valores[i].adjacentes[j].vertice.rotulo == atual.rotulo:
            print(f"{i + 1} - {self.valores[i].rotulo} - {self.valores[i].adjacentes[j].custo}")

# Classe que realiza a busca Gulosa
class Gulosa:
  def __init__(self, objetivo):
    self.objetivo = objetivo
    self.encontrado = False                                   #indica se o objetivo foi encontrado
    self.estacoes = []

  def buscar(self, atual):                                    #vai analisar o elemento que está sendo analisado no momento
    print('-------')
    print(f'Atual: {atual.rotulo}')                           #atual: nome da cidade
    atual.visitado = True
    self.estacoes.append(atual.rotulo)

    if atual == self.objetivo:
      print("Voce chegou no seu destino.\n")
      self.encontrado = True
    else:                                                     #buscador será uma função recursiva que pára quando self.encontrado
      vetor_ordenado = VetorOrdenado(len(atual.adjacentes))   #número de adjacentes define o tamanho do vetor a ser criado
      for adjacente in atual.adjacentes:                      #percorre cada adjacente
        if not adjacente.vertice.visitado:
          vetor_ordenado.insere(adjacente.vertice)            #adiciona as cidades adjacentes no vetor
      vetor_ordenado.imprime(atual)

      if vetor_ordenado.valores[0] is not None:                   #se o vetor não estiver vazio executa-se nova busca
        self.buscar(vetor_ordenado.valores[0])
      else:
        print("Impossivel encontrar o destino final com a Busca Gulosa.\n")

  def retonar_estacoes(self):
    if self.encontrado:   
      return self.estacoes
    else:
      return False