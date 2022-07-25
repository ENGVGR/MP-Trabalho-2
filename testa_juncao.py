"""
Teste para as funções em juncao.py
"""

from juncao import ler_arquivo

def test_ler_arquivo():
  arquivo_teste = ["1\n", "2\n", "3\n", "4\n", "5"]
  assert ler_arquivo("./exemplos/ex1.txt") == arquivo_teste