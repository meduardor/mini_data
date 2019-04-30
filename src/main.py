#!/usr/bin/env python3


import writer
import read

nameEx = input('Qual extensão json/csv: ').upper()
dataName = input('Nome do Banco: ').upper()
dataKeys = input('Nome da Chave: ')
dataValues = input('Nome dos Valores: ')


if __name__ == '__main__':

    if nameEx == "JSON":
        bancoData = writer.documentJson(dataName)
        bancoProduct = writer.writerDatajson(dataKeys, dataValues, dataName)
        readname = read.ReadDataJson(bancoData)
    elif nameEx == "CSV":
        pass
        # res = bancoProduct.table.rowsKeys()
    print(bancoData, bancoProduct)
    # print(res)
