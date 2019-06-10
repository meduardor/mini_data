#!/usr/bin/env python3

# Modulo Writer


import os
import json
import csv


class WriterJson():
    '''Escreve documentos Json'''

    def __init__(self, lista_key, lista_value, filename):
        self.lista_key = lista_key
        self.lista_value = lista_value
        self.filename = filename

    def DocJson(self):
        '''Cria arquivo Json'''
        caminho = '.dataset/'
        arquivo = caminho + (self.filename + ".json")
        if not os.path.exists(caminho):
            os.makedirs(caminho)
        if not os.path.exists(arquivo):
            open(arquivo, 'w')

    def DataJson(self, *data):
        for i in self.lista_key:
            self.lista_key.append(data)
        for x in self.lista_value:
            self.lista_value(data)

    def ConvertJson(self):
        '''Converte Dict Python em dados Json'''
        __lista_salvar = [dict(zip(WriterJson.DataJson(self.lista_key),
                                   WriterJson.DataJson(self.lista_value)))]
        __dictData = {"Dados": __lista_salvar}
        __dictData = json.dumps(__dictData,
                                indent=4,
                                sort_keys=False)
        try:
            arquivo = WriterJson.DocJson(self.filename)
            # TODO: Ver se o uso da função dentro da classe é dessa forma
            abrir = open(arquivo, 'r+')
            conteudo = arquivo.readlines()
            conteudo.append(__dictData)
            abrir = open(arquivo, 'w')
            abrir.writelines(conteudo)
            abrir.close()
        except Exception as Error:
            print("Não foi possivel escrever os Dados {}, {}"
                  .format(__dictData, Error))


class WriterCsv():
    '''Escrever documento csv'''

    def __init__(self, fieldcampos, fieldnames, filename):
        self.fieldcampos = fieldcampos
        self.fieldnames = fieldnames
        self.filename = filename

    def DocCsv(self):
        __caminho = '.dataset/'
        __arquivo = __caminho + (self.filename + ".csv")
        if not os.path.exists(__caminho):
            os.makedirs(__caminho)
        if not os.path.exists(__arquivo):
            open(__arquivo, 'w')

    def DataCsv(self, **data):
        self.fieldnames = []
        self.fieldcampos = []
        for i in self.fieldnames:
            self.fieldnames.append(data)

        for x in self.fieldcampos:
            self.fieldcampos.append(data)

    def WriterDataCsv(self, **data):
        arquivo = WriterCsv.DocCsv(self.filename)
        with open(arquivo, 'w+', newlines='') as csvfile:
            datawriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|',
                                    quoting=csv.QUOTE_MINIMAL)
            datawriter.writerow(data)

    # TODO: pensar a forma de passar os **args
    # TODO: E de escrever eles no Documento
