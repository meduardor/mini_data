#!/usr/bin/env python3


import os
import json
import csv

# TODO: Escerver todos os dados e imprimir na tela
# TODO: Filtrar os dados e imprimir
# NOTE: Todo o dict vai ter uma chave chamada  "Dados",
# TODO: Criar argumentos para interagir com os dados na visualização


class Read:
    filename: str


class ReadJson():
    def __init__(self, filename):
        self.filename = filename

    def DataJson(self):
        '''Leitura de dados de arquivos json'''

        # Verificação da existencia do arquivo
        __caminho = '.dataset/'
        __arquivo = __caminho + (self.filename + '.json')
        if not os.path.exists(__caminho):
            print('Esse caminho não existe')
        else:
            pass
        if not os.path.exists(__arquivo):
            print('Esse arquivo não existe')
        else:
            pass
        # Conversão e leitura do Arquivo ".JSON"
        try:
            fileJson = json.loads(__arquivo,
                                  encoding='UTF-8')
            with open(fileJson, 'r') as f_json:
                f_json.readlines()

                return print(f"Seu arquivo exite, {fileJson}")
        except TypeError:
            print("Seu arquivo não existe")

    def seeDoc(self, **data):
        # Acessa todos os dados do Dict
        __verdados = ReadJson.DataJson(self.filename)
        return __verdados

    def seeData(self, number=int, position=int):
        pass

        # TODO: Escrever os acessos por campos dentro do registros
        # Classe para leitura de arquivos csv


class ReadCsv():
    def __init__(self, filename):
        self.filename = filename

    def DataCsv(self, **data):
        __caminho = '.dataset/csv/'
        __arquivo = __caminho + (self.filename + '.csv')
        if not os.path.exists(__caminho):
            print("Esse caminho não existe")
        else:
            pass
        if not os.path.exists(__arquivo):
            print("Esse arquivo não existe")
        else:
            pass

        try:
            __arquivo_csv = ReadCsv.DataCsv(self.filename)
            with open(__arquivo_csv, newline='') as csvfile:
                __reader = csv.DicReader(csvfile)
                for row in __reader:
                    print(row[data], row[data])
        except TypeError:
            print("Erro de Leitura")

    def verCsv(self):
        __verdados_csv = ReadCsv.DataCsv(self.filename)
        return __verdados_csv
