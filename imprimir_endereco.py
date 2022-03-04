#PRECISA INSTALAR A BIBLIOTECA pywin32 
#PRECISA TER UM LEITOR DE PDF PS. DENTRO DO LEITOR DEFINIR OS PARAMETROS DE IMPRESSAO
#PRECISA SELECIONAR A IMPRESSORA QUE VAI IMPRIMIR E PASSANDO O SEQUENCIA E NOME DA IMPRESSORA
#PRECISA COLOCAR OS ARQUIVOS DENTRO DA PASTA 

import win32print
import win32api
import os

# Selecionar a impressora para impressão
lista_impressoras = win32print.EnumPrinters(2)
impressora = lista_impressoras[0]

win32print.SetDefaultPrinter(impressora[2])

#mandar imprimir todos os arquivos da pasta:
caminho = r"ENDERECO DA PASTA"
lista_arquivos = os.listdir(caminho)

for arquivo in lista_arquivos:
    win32api.ShellExecute(0,"print", arquivo, None, caminho, 0)

print("Impressão OK")