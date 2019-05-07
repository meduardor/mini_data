#!/usr/bin/env python3


import writer
# import read

nameEx = input('Qual extensão? json/csv.\n > ').upper()
dataName = input('Nome do Banco\n > ').upper()
count = int(input('Quantidade de dados.\n > '))


if __name__ == '__main__':
    stopdata = 0
    while True:
        if stopdata <= count:
            stopdata += 1
            if nameEx == "JSON":
                bancoProduct = writer.writerDatajson(dataName, count)
            elif nameEx == "CVS":
                pass
        elif stopdata >= count:
            break
