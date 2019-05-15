#!/usr/bin/env python3


import writer
import read

nameEx = input('Qual extensão? json/csv.\n > ').upper()
dataName = input('Nome do Banco\n > ').upper()
count = int(input('Quantidade de dados.\n > '))

# TODO: Definir funções de saida para cada tarefa

if __name__ == '__main__':
    stopdata = 0
    while True:
        if stopdata <= count:

            stopdata += 1
            if nameEx == "JSON":

                bancoProduct = writer.writerDatajson(dataName)
                results = read.ReadDataJson(dataName)
                print('Docmunet \n {}'.format(results))

            elif nameEx == "CSV":

                bancoCsv = writer.writerDataCsv(dataName)

        elif stopdata >= count:
            break
