"""
Teste para as funções em juncao.py
"""

from juncao import ler_arquivo
from juncao import menor_valor
from juncao import string_para_inteiro
from juncao import executar

def teste_ler_arquivo():
  linhas_teste = ["1\n", "2\n", "3\n", "4\n", "5"]
  assert ler_arquivo("./exemplos/ex1.txt") == linhas_teste

def teste_menor_valor():
  assert menor_valor(1, 2) == "Primeiro"
  assert menor_valor(1, 1) == "Iguais"
  assert menor_valor(2, 1) == "Segundo"
  assert menor_valor(4, 6) == "Primeiro"
  assert menor_valor(8, 2) == "Segundo"
  assert menor_valor(7, 7) == "Iguais"
  assert menor_valor(3, 9) == "Primeiro"
  assert menor_valor(4, 20) == "Primeiro"
  assert menor_valor(10, 10) == "Iguais"
  assert menor_valor(10, 4) == "Segundo"
  assert menor_valor(100, 40) == "Segundo"
  assert menor_valor(1000, 400) == "Segundo"

def teste_string_para_inteiro():
  linhas_teste = ["1\n", "2\n", "3\n", "4\n", "5"]
  assert string_para_inteiro(linhas_teste, 0) == 1
  assert string_para_inteiro(linhas_teste, 1) == 2
  assert string_para_inteiro(linhas_teste, 2) == 3
  assert string_para_inteiro(linhas_teste, 3) == 4
  assert string_para_inteiro(linhas_teste, 4) == 5

def teste_executar():
  executar("./exemplos/ex4.txt", "./exemplos/ex5.txt", "./exemplos/resultado3.txt")
  assert ler_arquivo("./exemplos/resultado3.txt")  == ler_arquivo("./exemplos/ex6.txt")