'''
    Metodos do sistema
'''
from os import path, makedirs
from subprocess import check_output
from zipfile import ZipFile, BadZipfile

import requests

from filiado import Filiado
from flask import (
    Blueprint, request, current_app, send_from_directory, render_template
)
CONST_URL = "http://agencia.tse.jus.br/estatistica/sead/eleitorado/filiados/uf/filiados_"
CONST_CSV_FOLDER = "/aplic/sead/lista_filiados/uf/"
ARRAY_UFS = ["ac", "al", "am", "ap", "ba", "ce", "df", "es", "go", "ma", "mt", "ms", "mg",
             "pa", "pb", "pr", "pe", "pi", "rj", "rn", "rs", "ro", "rr", "sc", "se", "sp", "to"]
ARRAY_PARTIDOS = ["dem", "novo", "pem", "pc_do_b", "pcb", "pco", "pdt", "phs", "pmdb", "pmb",
                  "pmn", "pp", "ppl", "pps", "pr", "prb", "pros", "prp", "prtb", "psb",
                  "psc", "psb", "psdb", "psdc", "psl", "psol", "pstu", "pt", "pt_do_b", "ptb",
                  "ptn", "ptc", "pv", "rede", "sd"]
ARRAY_ERROS = []
ARRAY_FILIADOS = []

filiados_blueprint = Blueprint('filiados', __name__,url_prefix="/filiados", )

@filiados_blueprint.route('/')
def main():
    """
    Rota principal da aplicacao
    """
    #findbynameanduf('NIA', 'ce')
    return render_template('index.html')

@filiados_blueprint.route('/download')
def download():
    """
    Download a lista de filiados da pagina do TSE
    """
    if not path.exists('./files/'):
        makedirs('./files/')
    for estado in ARRAY_UFS:
        for partido in ARRAY_PARTIDOS:

            endereco = CONST_URL + partido + '_' + estado + '.zip'

            print endereco

            response = requests.get(endereco, stream=True)

            caminho = './files/' + estado + '/'
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

@filiados_blueprint.route('/consultar', methods=['GET', 'POST'])
def consultar():
    """
    Consultar Filiados
    """    

    if request.method == 'POST':
        nome = request.form.get('nome')
        estado = request.form.get('estado')
        print '\n\n' + nome + ' - ' + estado + '\n\n'
        if estado != '':
            lista_filiados = findbynameanduf(nome.upper(), estado)
        #print ARRAY_FILIADOS[0].nome

    return render_template('index.html', filiados=lista_filiados, err=ARRAY_ERROS)

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

    #print '\n\n' + aux + '\n\n'
    retorno = []
    try:
        for item in aux:

            print item
            fil = Filiado(item.encode(encoding='UTF-8'))

            #print '\n\n' + fil + '\n\n'

            retorno.append(fil)
    except Exception as err:
        print err
    return retorno
