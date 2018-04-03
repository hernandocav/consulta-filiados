'''
    Metodos do sistema
'''
from os import path
from os import makedirs
from subprocess import check_output
from zipfile import ZipFile, BadZipfile

import requests
from filiado import Filiado
from flask import request, current_app, send_from_directory, render_template

from config import *

from app import app

@app.route('/')  
def main():
    """
    Rota principal da aplicacao
    """
    findbynameanduf('NIA', 'ce')
    return render_template('index2.html')

@app.route('/download')
def download():
    """
    Download a lista de filiados da pagina do TSE
    """
    if not path.exists('./files/filiados/'):
        makedirs('./files/filiados/')
    for estado in ARRAY_UFS:
        for partido in ARRAY_PARTIDOS:

            endereco = CONST_URL + partido + '_' + estado + '.zip'

            print endereco

            response = requests.get(endereco, stream=True)            

            caminho = './files/filiados/' + estado + '/'
            arquivo = 'filiados_' + partido + '_' + estado + '.zip'

            if not path.exists(caminho):
                makedirs(caminho)
            output = open(caminho + arquivo, "wb")
            output.write(response.content)
            output.close()

            try:
                target = caminho + arquivo
                # print 'target ' + target
                with ZipFile(target) as zip_ref:
                    zip_ref.extractall(caminho)
                    zip_ref.close()
            except BadZipfile:
                ARRAY_ERROS.append('ZIP COM ERRO: ' + caminho + arquivo)
                print 'ZIP COM ERRO: ' + caminho + arquivo
                continue
    return render_template('index.html')

@app.route('/consultar/<estado>/<nome>')
def consultar(estado, nome):
    """
    Consultar Filiado
    """
    print '\n\n' + nome + ' - ' + estado + '\n\n'
    findbynameanduf(nome.upper(), estado)
    return render_template('index2.html')

def findbynameanduf(nome, estado):
    """
    Procura pelo nome do filiado nos aquivos do TSE
    """
    caminho = './files/' + estado
    cmd = ('/usr/bin/iconv -f iso-8859-1 -t UTF-8 ' + caminho + CONST_CSV_FOLDER
           + '* | /bin/grep  \"' + nome.upper() + '\"')

    print '\n\n' + cmd + '\n\n'

    resultado = check_output(cmd, shell=True)
    aux = resultado.decode(encoding='UTF-8').splitlines()

    print '\n\n' + aux + '\n\n'

    try:
        for item in aux:
            fil = Filiado.__novo__(Filiado, item)

            print '\n\n' + fil + '\n\n'

            ARRAY_FILIADOS.append(fil)
    except Exception as err:
        print err
