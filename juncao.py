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
  return int(linhas[indice])

def caminho_percorrido(caminho, primeiro=False):
  if primeiro:
    if caminho == "D":
      with open('./exemplos/caminhos.txt', 'w') as arq:
        arq.write("D\n")
    else:
      with open('./exemplos/caminhos.txt', 'w') as arq:
        arq.write(caminho)
  else:
    if caminho == "D":
      with open('./exemplos/caminhos.txt', 'a') as arq:
        arq.write("D\n")
    else:
      with open('./exemplos/caminhos.txt', 'a') as arq:
        arq.write(caminho)


def executar(arquivo_1, arquivo_2, arquivo_resultante, primeiro):
  caminho_percorrido("A",primeiro)
  linhas_1 = ler_arquivo(arquivo_1) 
  linhas_2 = ler_arquivo(arquivo_2) 
  caminho_percorrido("BC")
  ultimo = False
  

  with open(arquivo_resultante, "w", encoding="utf-8") as arquivo_resultante_aberto:
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
          arquivo_resultante_aberto.writelines(str(valor_2) + "\n")
          linhas_2.pop(0)
          caminho_percorrido("H")

    arquivo_resultante_aberto.close()

  caminho_percorrido("D")
