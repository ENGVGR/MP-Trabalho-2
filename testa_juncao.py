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
  executar("./exemplos/ex2.txt", "./exemplos/ex2.txt", "./exemplos/resultado.txt", True)
  assert ler_arquivo("./exemplos/resultado.txt")  == ler_arquivo("./exemplos/ex2.txt")
  assert ler_arquivo("./exemplos/caminhos.txt")  == ["ABCED\n"]

  executar("./exemplos/ex3.txt", "./exemplos/ex4.txt", "./exemplos/resultado.txt", False)
  assert ler_arquivo("./exemplos/resultado.txt")  == ler_arquivo("./exemplos/ex5.txt")
  assert ler_arquivo("./exemplos/caminhos.txt")  == ["ABCED\n", "ABCEFGD\n"]

  executar("./exemplos/ex3.txt", "./exemplos/ex3.txt", "./exemplos/resultado.txt", False)
  assert ler_arquivo("./exemplos/resultado.txt")  == ler_arquivo("./exemplos/ex6.txt")
  assert ler_arquivo("./exemplos/caminhos.txt")  == ["ABCED\n", "ABCEFGD\n", "ABCEFHD\n"]

  executar("./exemplos/ex4.txt", "./exemplos/ex3.txt", "./exemplos/resultado.txt", False)
  assert ler_arquivo("./exemplos/resultado.txt")  == ler_arquivo("./exemplos/ex5.txt")
  assert ler_arquivo("./exemplos/caminhos.txt")  == ["ABCED\n", "ABCEFGD\n", "ABCEFHD\n", "ABCEFID\n"]

  executar("./exemplos/ex7.txt", "./exemplos/ex8.txt", "./exemplos/resultado.txt", False)
  assert ler_arquivo("./exemplos/resultado.txt")  == ler_arquivo("./exemplos/ex9.txt")
  assert ler_arquivo("./exemplos/caminhos.txt")  == ["ABCED\n", "ABCEFGD\n", "ABCEFHD\n", "ABCEFID\n", "ABCEFGFGFGD\n"]

  executar("./exemplos/ex10.txt", "./exemplos/ex11.txt", "./exemplos/resultado.txt", False)
  assert ler_arquivo("./exemplos/resultado.txt")  == ler_arquivo("./exemplos/ex12.txt")
  assert ler_arquivo("./exemplos/caminhos.txt")  == ["ABCED\n", "ABCEFGD\n", "ABCEFHD\n", "ABCEFID\n", "ABCEFGFGFGD\n", "ABCEFGFGFHD\n"]

  executar("./exemplos/ex13.txt", "./exemplos/ex14.txt", "./exemplos/resultado.txt", False)
  assert ler_arquivo("./exemplos/resultado.txt")  == ler_arquivo("./exemplos/ex9.txt")
  assert ler_arquivo("./exemplos/caminhos.txt")  == ["ABCED\n", "ABCEFGD\n", "ABCEFHD\n", "ABCEFID\n", "ABCEFGFGFGD\n", "ABCEFGFGFHD\n", "ABCEFGFGFID\n"]

  executar("./exemplos/ex15.txt", "./exemplos/ex16.txt", "./exemplos/resultado.txt", False)
  assert ler_arquivo("./exemplos/resultado.txt")  == ler_arquivo("./exemplos/ex17.txt")
  assert ler_arquivo("./exemplos/caminhos.txt")  == ["ABCED\n", "ABCEFGD\n", "ABCEFHD\n", "ABCEFID\n", "ABCEFGFGFGD\n", "ABCEFGFGFHD\n", "ABCEFGFGFID\n", "ABCEFGFHFGD\n"]

  executar("./exemplos/ex18.txt", "./exemplos/ex19.txt", "./exemplos/resultado.txt", False)
  assert ler_arquivo("./exemplos/resultado.txt")  == ler_arquivo("./exemplos/ex20.txt")
  assert ler_arquivo("./exemplos/caminhos.txt")  == ["ABCED\n", "ABCEFGD\n", "ABCEFHD\n", "ABCEFID\n", "ABCEFGFGFGD\n", "ABCEFGFGFHD\n", "ABCEFGFGFID\n", "ABCEFGFHFGD\n", "ABCEFGFHFHD\n"]

  executar("./exemplos/ex21.txt", "./exemplos/ex22.txt", "./exemplos/resultado.txt", False)
  assert ler_arquivo("./exemplos/resultado.txt")  == ler_arquivo("./exemplos/ex23.txt")
  assert ler_arquivo("./exemplos/caminhos.txt")  == ["ABCED\n", "ABCEFGD\n", "ABCEFHD\n", "ABCEFID\n", "ABCEFGFGFGD\n", "ABCEFGFGFHD\n", "ABCEFGFGFID\n", "ABCEFGFHFGD\n", "ABCEFGFHFHD\n", "ABCEFGFHFID\n"]
  