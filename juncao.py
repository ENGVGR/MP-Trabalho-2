"""
@file
Funções para juntar dois arquivos .txt ordenados em um arquivo .txt ordenado
"""

def ler_arquivo(arquivo):
  """! Abre o arquivo e armazena o seu conteudo na variável "linhas".
    @param arquivo  Arquivo em formato .txt.
    @return  Conteudo contido no arquivo
  """
  with open(arquivo, "r", encoding="utf-8") as arquivo_aberto:
    linhas = arquivo_aberto.readlines()
  return linhas

def menor_valor(valor_1, valor_2):
  """! Compara dois inteiros e retorna qual o menor.
    @param valor_1  Valor inteiro.
    @param valor_2  Valor inteiro.
    @return  Retorna qual o menor valor: "Primeiro", "Segundo" ou, caso sejam iguais, "Iguais"
  """
  if valor_1 < valor_2:
    return "Primeiro"
  elif valor_1 > valor_2:
    return "Segundo"
  else:
    return "Iguais"

def string_para_inteiro(linhas, indice):
  """! Converte a string da lista "linhas" em inteiro.
    @param linhas  Lista de elementos.
    @param indice  Valor inteiro do indice desejado.
    @return  Retorna o elemento, no indice fornecido, convertido para inteiro
  """
  return int(linhas[indice])

def caminho_percorrido(caminho, primeiro=False):
  """! Escreve no arquivo "caminhos" o caminho percorrido.
    @param caminho  Lista de elementos.
    @param primeiro  Valor booleano que representa se é o primeiro termo do arquivo.
  """
  caminhos = "./exemplos/caminhos.txt"
  if primeiro:
    if caminho == "D":
      with open(caminhos, "w", encoding="utf-8") as arq:
        arq.write("D\n")
    else:
      with open(caminhos, "w", encoding="utf-8") as arq:
        arq.write(caminho)
  else:
    if caminho == "D":
      with open(caminhos, "a", encoding="utf-8") as arq:
        arq.write("D\n")
    else:
      with open(caminhos, "a", encoding="utf-8") as arq:
        arq.write(caminho)


def executar(arquivo_1, arquivo_2, arquivo_resultante, primeiro):
  """! Função que executa o programa de ler 2 arquivos e combiná-los ordenadamente. E armazenar o caminho percorrido durante esse processo. Para isso são comparados cada valor de um arquivo com o outro e escrito no arquivo resultante o menor dentre esses valores.
    @param arquivo_1  Arquivo .txt que será lido.
    @param arquivo_2  Arquivo .txt que será lido.
    @param arquivo_resultante  Arquivo .txt onde será armazenado o resultado.
    @param primeiro  Valor Booleano que define se é a primeira execução do programa ou não (para armazenar todos os caminhos em um único arquivo).
  """
  caminho_percorrido("A",primeiro)
  linhas_1 = ler_arquivo(arquivo_1)
  linhas_2 = ler_arquivo(arquivo_2)
  caminho_percorrido("BC")
  ultimo = False

  with open(arquivo_resultante, "w",
    encoding="utf-8") as arquivo_resultante_aberto:
    caminho_percorrido("E")
    while len(linhas_1) + len(linhas_2) > 0:

      if len(linhas_1) + len(linhas_2) == 1:
        ultimo = True

      if len(linhas_1) == 0 or len(linhas_2) == 0:

        if len(linhas_1) > 0:
          valor_1 = string_para_inteiro(linhas_1, 0)

          if ultimo:
            arquivo_resultante_aberto.writelines(str(valor_1))

          else:
            arquivo_resultante_aberto.writelines(str(valor_1) + "\n")
          linhas_1.pop(0)

        else:
          valor_2 = string_para_inteiro(linhas_2, 0)

          if ultimo:
            arquivo_resultante_aberto.writelines(str(valor_2))

          else:
            arquivo_resultante_aberto.writelines(str(valor_2) + "\n")
          linhas_2.pop(0)

      else:
        caminho_percorrido("F")
        valor_1 = string_para_inteiro(linhas_1, 0)
        valor_2 = string_para_inteiro(linhas_2, 0)

        if menor_valor(valor_1, valor_2) == "Primeiro":
          arquivo_resultante_aberto.writelines(str(valor_1) + "\n")
          linhas_1.pop(0)
          caminho_percorrido("G")

        elif menor_valor(valor_1, valor_2) == "Segundo":
          arquivo_resultante_aberto.writelines(str(valor_2) + "\n")
          linhas_2.pop(0)
          caminho_percorrido("I")

        else:
          if len(linhas_1) + len(linhas_2) == 2:
            arquivo_resultante_aberto.writelines(str(valor_1) + "\n")
            arquivo_resultante_aberto.writelines(str(valor_2))
            linhas_1.pop(0)
            linhas_2.pop(0)
          else:
            arquivo_resultante_aberto.writelines(str(valor_1) + "\n")
            arquivo_resultante_aberto.writelines(str(valor_2) + "\n")
            linhas_1.pop(0)
            linhas_2.pop(0)
          caminho_percorrido("H")

    arquivo_resultante_aberto.close()

  caminho_percorrido("D")
