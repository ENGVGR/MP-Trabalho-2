"""
@file testa_juncao.py
Teste para as funções em juncao.py
"""

# Imports
from juncao import ler_arquivo
from juncao import menor_valor
from juncao import string_para_inteiro
from juncao import executar

def teste_ler_arquivo():
  """! Testa a abertura e leitura dos arquivos.
    Para isso é fornecido o arquivo para a função "ler_arquivo) e comparado com a linhas_teste que representa o resultado esperado
  """
  linhas_teste = ["1\n", "2\n", "3\n", "4\n", "5"]
  assert ler_arquivo("./exemplos/ex1.txt") == linhas_teste

def teste_menor_valor():
  """! Testa se a função "menor_valor" retorna o menor valor.
    Para isso é fornecido dois valores e é comparado ao resultado esperado
  """
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
  """! Testa se a função "string_para_inteiro" retorna o valor convertido em inteiro.
    Para isso é fornecido dois valores, a lista de elementos e o indice do elemento desejado. 
    Ao final é comparado com o resultado esperado.
  """
  linhas_teste = ["1\n", "2\n", "3\n", "4\n", "5"]
  assert string_para_inteiro(linhas_teste, 0) == 1
  assert string_para_inteiro(linhas_teste, 1) == 2
  assert string_para_inteiro(linhas_teste, 2) == 3
  assert string_para_inteiro(linhas_teste, 3) == 4
  assert string_para_inteiro(linhas_teste, 4) == 5

def teste_executar():
  """! Testa a execução do programa inteiro, inclusive se os caminhos percorridos estão sendo armazenados.
    Para isso é fornecido 4 valores para a função "executar", que são os dois arquivos que serão combinados, 
    o arquivo onde será armazenado o resultado e um valor booleano indicano se é a primeira execução da função ou não.
    Ao final é comparado aos resultados esperados.
  """
  resultado = "./exemplos/resultado.txt"
  exemplo = "./exemplos/ex"
  caminhos = ["ABCED\n", "ABCEFGD\n", "ABCEFHD\n", "ABCEFID\n", "ABCEFGFGFGD\n",
    "ABCEFGFGFHD\n", "ABCEFGFGFID\n", "ABCEFGFHFGD\n", "ABCEFGFHFHD\n",
    "ABCEFGFHFID\n"]

  executar(exemplo + "2.txt", exemplo + "2.txt", resultado, True)
  assert ler_arquivo(resultado)  == ler_arquivo(exemplo + "2.txt")
  assert ler_arquivo("./exemplos/caminhos.txt")  == caminhos[0:1]

  executar(exemplo + "3.txt", exemplo + "4.txt", resultado, False)
  assert ler_arquivo(resultado)  == ler_arquivo(exemplo + "5.txt")
  assert ler_arquivo("./exemplos/caminhos.txt")  == caminhos[0:2]

  executar(exemplo + "3.txt", exemplo + "3.txt", resultado, False)
  assert ler_arquivo(resultado) == ler_arquivo(exemplo + "6.txt")
  assert ler_arquivo("./exemplos/caminhos.txt")  == caminhos[0:3]

  executar(exemplo + "4.txt", exemplo + "3.txt", resultado, False)
  assert ler_arquivo(resultado)  == ler_arquivo(exemplo + "5.txt")
  assert ler_arquivo("./exemplos/caminhos.txt")  == caminhos[0:4]

  executar(exemplo + "7.txt", exemplo + "8.txt", resultado, False)
  assert ler_arquivo(resultado)  == ler_arquivo(exemplo + "9.txt")
  assert ler_arquivo("./exemplos/caminhos.txt")  == caminhos[0:5]

  executar(exemplo + "10.txt", exemplo + "11.txt", resultado, False)
  assert ler_arquivo(resultado)  == ler_arquivo(exemplo + "12.txt")
  assert ler_arquivo("./exemplos/caminhos.txt")  == caminhos[0:6]

  executar(exemplo + "13.txt", exemplo + "14.txt", resultado, False)
  assert ler_arquivo(resultado)  == ler_arquivo(exemplo + "9.txt")
  assert ler_arquivo("./exemplos/caminhos.txt")  == caminhos[0:7]

  executar(exemplo + "15.txt", exemplo + "16.txt", resultado, False)
  assert ler_arquivo(resultado)  == ler_arquivo(exemplo + "17.txt")
  assert ler_arquivo("./exemplos/caminhos.txt")  == caminhos[0:8]

  executar(exemplo + "18.txt", exemplo + "19.txt", resultado, False)
  assert ler_arquivo(resultado)  == ler_arquivo(exemplo + "20.txt")
  assert ler_arquivo("./exemplos/caminhos.txt")  == caminhos[0:9]

  executar(exemplo + "21.txt", exemplo + "22.txt", resultado, False)
  assert ler_arquivo(resultado)  == ler_arquivo(exemplo + "23.txt")
  assert ler_arquivo("./exemplos/caminhos.txt")  == caminhos[0:10]
