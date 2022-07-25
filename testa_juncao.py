"""
Teste para as funções em juncao.py
"""

from juncao import ler_arquivo

def test_ler_arquivo():
  arquivo_teste = ["1", "2", "3", "4", "5"]
  assert ler_arquivo("ex1.txt") == arquivo_teste