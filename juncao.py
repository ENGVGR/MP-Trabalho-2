"""
Funções para juntar dois arquivos .txt ordenados em um arquivo .txt ordenado
"""

def ler_arquivo(arquivo):
  arquivo = open(arquivo)
  linhas = arquivo.readlines()
  return linhas
