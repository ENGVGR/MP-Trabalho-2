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

def executar(arquivo_1, arquivo_2, arquivo_resultante):
  linhas_1 = ler_arquivo(arquivo_1) 
  linhas_2 = ler_arquivo(arquivo_2) 
  ultimo = False

  with open(arquivo_resultante, "w", encoding="utf-8") as arquivo_resultante_aberto:
    while len(linhas_1) + len(linhas_2) > 0:

      if len(linhas_1) + len(linhas_2) == 1:
        ultimo = True

      if len(linhas_1) == 0 or len(linhas_2) == 0:

        if len(arquivo_1) > 0:
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
        valor_1 = string_para_inteiro(linhas_1, 0)
        valor_2 = string_para_inteiro(linhas_2, 0)

        if menor_valor(valor_1, valor_2) == "Primeiro":
          arquivo_resultante_aberto.writelines(str(valor_1) + "\n")
          linhas_1.pop(0)

        else:
          arquivo_resultante_aberto.writelines(str(valor_2) + "\n")
          linhas_2.pop(0)

    arquivo_resultante_aberto.close()
