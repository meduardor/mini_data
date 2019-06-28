#!/usr/bin/env python3

import os
# import json
from writer import WriterCsv
from writer import WriterJson
from read import ReadJson

# TODO: Definir funções de saida para cada tarefa
# TODO: Criar uma Chave primaria para identificar os dados.


def escrever_json(arquivo, lista_key, lista_value, *data):
    # TODO: Refatorar essa função de acordo com as novas funcionalidades do
    # Criação da base de dados in JSON
    escrita_json = WriterJson.DocJson(arquivo)

    # Número definido para entrada de e dados
    count = int(input('Quantos dados vai escrever: '))
    lista_key = []
    lista_value = []

    # Listas de dados
    data_json_value = WriterJson(lista_key, lista_value)
    data_json_key = WriterJson(lista_key, lista_value)

    # Chamada do Modulo writer e das funções de escritas Json
    # TODO: Fazer testes sobre a entrada de dados das lista.
    # condicional de entrada de dados
    # TODO(merds): Modificar o loop de entrada de dados.

    if lista_key == [] and os.path.exists(escrita_json):
        with open(escrita_json, 'r+') as f:
            f.readlines()
            for element in range(count):
                lista_key.append(data_json_key.DataJson(escrita_json,
                                                        data))
    else:
        pass
    if lista_value == []:
        for element in range(count):
            lista_value.append(
                data_json_value.DataJson(escrita_json, data_json_value),
                data_json_value.dataJson_value()
            )
    else:
        pass

    # Converte os dos da lista em Dict e grava no arquivo JSON
    # escrita_dados_json = {}
    escrita_dados_json = WriterJson(lista_key, lista_value)
    escrita_dados_json.ConvertJson(data_json_key,
                                   data_json_value,
                                   escrita_json)
    return escrita_dados_json


def escrever_csv():
    escrita_csv = WriterCsv.DocCsv(nameEx)
    dados_csv = WriterCsv.DataCsv(dataName)
    escrita_dados_csv = WriterCsv.WriterDataCsv(escrita_csv, dados_csv)
    return escrita_dados_csv


def ver_json(name):
    '''Ver os dados do Documento json'''
    verDados = ReadJson.verDoc(name)
    return verDados


def ver_csv():
    pass


def backup():
    pass


def connection():
    pass


def users():
    pass


if __name__ == '__main__':
    lista_key = []
    lista_value = []
    nameEx = input('Qual extensão? json/csv.\n > ').upper()
    dataName = input('Nome do Banco\n > ').upper()
    count = int(input('Quantidade de dados.\n > '))

    stopdata = 0
    while True:
        if stopdata <= count:
            stopdata += 1
            if nameEx == 'JSON':
                escrever_json(dataName, lista_key, lista_value)
            elif nameEx == 'CSV':
                pass
            else:
                pass

        elif stopdata >= count:
            break
