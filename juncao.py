"""
Funções para juntar dois arquivos .txt ordenados em um arquivo .txt ordenado
"""

def ler_arquivo(arquivo):
  with open(arquivo, "r", encoding="utf-8") as arquivo_aberto:
    linhas = arquivo_aberto.readlines()
  return linhas

def menor_valor(valor_1, valor_2):
  if valor_1 < valor_2:
    return "Primeiro"
  elif valor_1 > valor_2:
    return "Segundo"
  else:
    return "Iguais"

def string_para_inteiro(linhas, indice):
  return int(linhas[indice][0])
