#!/usr/bin/env python3


import os
import json


# TODO: Escerver todos os dados e imprimir na tela
# TODO: Filtrar os dados e imprimir
# NOTE:  Todo o dict vai ter uma chave chamada  "Dados",
# Seguido de uma lista.

class ReadJson():
    def __init__(self, filename):
        self.filename = filename

    def DataJson(self):
        '''Leitura de dados de arquivos json'''

        # Verificação da existencia do arquivo
        caminho = '.dataset/'
        arquivo = caminho + (self.filename + '.json')
        if not os.path.exists(caminho):
            print('Esse caminho não existe')
        else:
            pass
        if not os.path.exists(arquivo):
            print('Esse arquivo não existe')
        else:
            pass
        # Conversão e leitura do Arquivo ".JSON"
        try:
            fileJson = json.loads(arquivo,
                                  encoding='UTF-8')
            with open(fileJson, 'r') as f_json:
                f_json.readlines()

                return print(f"Seu arquivo exite, {fileJson}")
        except TypeError:
            print("Seu arquivo não existe")

    def verDoc(self):
        __verdados = ReadJson.DataJson(self.filename)
        return __verdados


class ReadCsv():
    def __init__(self, filename):
        self.filename = filename

    def ReadDataCsv(filename):
        pass
