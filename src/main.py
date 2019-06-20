#!/usr/bin/env python3

import os
import json
from writer import WriterCsv
from writer import WriterJson
from read import ReadJson

# TODO: Definir funções de saida para cada tarefa
# TODO: Criar uma Chave primaria para identificar os dados.


def escrever_json(name):
    # TODO: Refatorar essa função de acordo com as novas funcionalidades do
    # Criação da base de dados in JSON
    escrita_json = WriterJson.DocJson(name)

    # Número definido para entrada de e dados
    count = int(input('Quantos dados vai escrever: '))

    # Listas de dados
    data_json_value = []
    data_json_key = []

    # Chamada do Modulo writer e das funções de escritas Json
    # dados_json_key = WriterJson(data_json_key, data_json_value)
    # dados_json_value = WriterJson(data_json_key, data_json_value)

    for i in range(count):
        data_json_key.append(input('Digite nome dos Campos: '))
    # TODO: Fazer testes sobre a entrada de dados das lista.
    # Condicional de entrada de dados
    data = json.loads(escrita_json)

    if not data_json_key == 0:
        if os.path.exists(escrita_json):
            with open(data, 'r') as f:
                f.readlines()
        elif data_json_key in f.readlines():
            pass
        else:
            dados_json_key = WriterJson.DataJson(escrita_json,
                                                 data_json_key)
    elif not data_json_value == 0:
        for x in range(count):
            data_json_value.append(input('Digite os valores: '))
            dados_json_value = WriterJson.DataJson(data_json_value,
                                                   escrita_json)
            dados_json_value.dataJson_value(escrita_json)
        else:
            pass

    # Converte os dos da lista em Dict e grava no arquivo JSON
    escrita_dados_json = WriterJson.ConvertJson(escrita_json,
                                                dados_json_key,
                                                dados_json_value)
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

    nameEx = input('Qual extensão? json/csv.\n > ').upper()
    dataName = input('Nome do Banco\n > ').upper()
    count = int(input('Quantidade de dados.\n > '))

    stopdata = 0
    while True:
        if stopdata <= count:
            stopdata += 1
            if nameEx == 'JSON':
                escrever_json(dataName)
            elif nameEx == 'CSV':
                pass
            else:
                pass

        elif stopdata >= count:
            break
