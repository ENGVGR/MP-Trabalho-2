"""
Funções para juntar dois arquivos .txt ordenados em um arquivo .txt ordenado
"""

def ler_arquivo(arquivo):
  with open(arquivo, "r", encoding="utf-8") as arq:
    linhas = arq.readlines()
  return linhas
