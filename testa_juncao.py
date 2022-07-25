"""
Teste para as funções em juncao.py
"""

from juncao import ler_arquivo
from juncao import menor_valor
from juncao import string_para_inteiro

def teste_ler_arquivo():
  linhas = ["1\n", "2\n", "3\n", "4\n", "5"]
  assert ler_arquivo("./exemplos/ex1.txt") == linhas

def teste_menor_valor():
  assert menor_valor(1, 2) == "Primeiro"
  assert menor_valor(1, 1) == "Iguais"
  assert menor_valor(2, 1) == "Segundo"
  assert menor_valor(4, 6) == "Primeiro"
  assert menor_valor(8, 2) == "Segundo"
  assert menor_valor(7, 7) == "Iguais"
  assert menor_valor(3, 9) == "Primeiro"

def teste_string_para_inteiro():
  linhas = ["1\n", "2\n", "3\n", "4\n", "5"]
  assert string_para_inteiro(linhas, 0) == 1
  assert string_para_inteiro(linhas, 1) == 2
  assert string_para_inteiro(linhas, 2) == 3
  assert string_para_inteiro(linhas, 3) == 4
  assert string_para_inteiro(linhas, 4) == 5
