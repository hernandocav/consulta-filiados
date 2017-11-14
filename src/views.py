'''
    Métodos do sistema
'''
from os import path
from os import makedirs
from subprocess import check_output
import zipfile
import requests
from filiado import Filiado


from app import app

from config import ARRAY_UFS
from config import ARRAY_FILIADOS
from config import ARRAY_PARTIDOS
from config import CONST_URL
from config import CONST_CSV_FOLDER
from config import ARRAY_ERROS

"""
    Handler principal da aplicação
"""
# @app.route('/test')  
# def main(self):
#     findbynameanduf("SÔNIA", "ce")
#     return self.render_response('index.html')

""" 
    Download a lista de filiados da página do TSE
"""
def download():
    if not path.exists("./files/"):
        makedirs("./files/")
    for estados in ARRAY_UFS:
        for partido in ARRAY_PARTIDOS:

            endereco = CONST_URL + partido + "_" + estados + ".zip"

            print(endereco)
            response = requests.get(endereco, stream=True)

            caminho = "./files/" + estados
            arquivo = "filiados_" + partido + "_" + estados + ".zip"

            if not path.exists(caminho):
                makedirs(caminho)
            output = open(caminho + "/" + arquivo, "wb")
            output.write(response.content)

            try:
                zip_ref = zipfile.ZipFile(caminho + "/" + arquivo, 'r')
                zip_ref.extractall(caminho + "/")
                zip_ref.close()
            except zipfile.BadZipFile:
                ARRAY_ERROS.append("ZIP COM ERRO: " + caminho + "/" + arquivo)
                print("ZIP COM ERRO: " + caminho + "/" + arquivo)
                continue
    return self.render_response('index.html')

"""
    Consultar
"""
def consultar(self):
    nome = self.request.get_param('nome')
    estado = self.request.get_param('estado')
    print("\n\n" + nome + " - " + estado + "\n\n")
    findbynameanduf(nome.upper(), estado)

def findbynameanduf(nome, estado):
    """
        Procura pelo nome do filiado nos aquivos do TSE
    """

    caminho = "./files/" + estado
    cmd = ("/usr/bin/iconv -f iso-8859-1 -t UTF-8 " + caminho + CONST_CSV_FOLDER
           + "* | /bin/grep  \"" + nome.upper() + "\"")

    print("\n\n" + cmd + "\n\n")

    resultado = check_output(cmd, shell=True)    

    aux = resultado.decode(encoding='UTF-8').splitlines()
    print("\n\n" + aux + "\n\n")

    try:
        for item in aux:
            fil = Filiado.__new__(Filiado, item)
            print("\n\n" + fil + "\n\n")
            ARRAY_FILIADOS.append(fil)
    except Exception as err:
        print(err)
