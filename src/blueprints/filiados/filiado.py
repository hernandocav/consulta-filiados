class Filiado():
    """
    Classe de Filiado
    """
    def __criar__(self, dt_extracao, hr_extracao, nr_inscricao, nome, sigla_partido, partido, estado,
                 codigo_municipio, municipio, zona, secao, situacao, tipo_registro,
                 dt_processamento, dt_desfiliacao, dt_filiacao, dt_cancelamento, dt_regularizacao,
                 motivo_cancelamento):
        self.dt_extracao = dt_extracao
        self.hr_extracao = hr_extracao
        self.nr_inscricao = nr_inscricao
        self.nome = nome
        self.sigla_partido = sigla_partido
        self.partido = partido
        self.estado = estado
        self.codigo_municipio = codigo_municipio
        self.municipio = municipio
        self.zona = zona
        self.secao = secao
        self.dt_filiacao = dt_filiacao
        self.situacao = situacao
        self.tipo_registro = tipo_registro
        self.dt_processamento = dt_processamento
        self.dt_desfiliacao = dt_desfiliacao
        self.dt_cancelamento = dt_cancelamento
        self.dt_regularizacao = dt_regularizacao
        self.motivo_cancelamento = motivo_cancelamento

    def __init__(self, texto):

        aux = str(texto).split("\";\"")
        
        self.dt_extracao = aux[0]
        self.hr_extracao = aux[1]
        self.nr_inscricao = aux[2]
        self.nome = aux[3]
        self.sigla_partido = aux[4]
        self.partido = aux[5]
        self.estado = aux[6]
        self.codigo_municipio = aux[7]
        self.municipio = aux[8]
        self.zona = aux[9]
        self.secao = aux[10]
        self.dt_filiacao = aux[11]
        self.situacao = aux[12]
        self.tipo_registro = aux[13]
        self.dt_processamento = aux[14]
        self.dt_desfiliacao = aux[15]
        self.dt_cancelamento = aux[16]
        self.dt_regularizacao = aux[17]
        self.motivo_cancelamento = aux[18]
        