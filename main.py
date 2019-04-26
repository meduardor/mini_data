#!/usr/bin/env python3


import writer


dataName = input('Nome do Banco: ')
dataKeys = input('Nome da Chave: ')
dataValues = input('Nome dos Valores: ')


if __name__ == '__main__':
    bancoData = writer.documentJson(dataName)
    bancoProduct = writer.writerData(dataKeys, dataValues)

    print(bancoData, bancoProduct)

