class Data():
    import logging

    log_format = '%(asctime)s:%(levelname)s:%(message)s'

    logging.basicConfig(filename='arquivo_log.log',
                        filemode='w',
                        level=logging.DEBUG,
                        format=log_format)

    def __init__(self):

        self.getfile()
        self.filejson()

    def getfile(self):
        import pysftp as sftp

        opts = sftp.CnOpts()
        opts.hostkeys = None

        host = "sftp.confere.com.br"
        port = 22
        username = 'desafio'
        password = 'N2JiYTcwMGYzNTFiYjZmMTE3YjJlYmNk'
        home = '/confere-data/sftp-users/desafio'

        self.logging.debug('Conecting...')

        with sftp.Connection(host=host, username=username, password=password, cnopts=opts) as s:
            self.logging.info('Connected')

            remoteFile = 'challenge_sales.csv'
            localFile = 'challenge_sales.csv'

            self.logging.info('Getting file')
            s.get(remoteFile, localFile)

            s.close()

        self.logging.info('Closed connection')

    def filejson(self):

        import csv
        import json
        from collections import OrderedDict

        arquivo = open('challenge_sales.csv', 'r')
        lista = csv.reader(arquivo, delimiter=';')

        data_dict = []

        # Trata o cabecalho
        first_line = arquivo.readline().rstrip()
        first_line = first_line.split(';')

        data_dict = [{
            'Tipo de Registro': first_line[0],
            'Codigo do Cliente': first_line[1],
            'Hora de criacao do arquivo': first_line[2],
            'Data de criacao do arquivo': first_line[3],
            'Versao do arquivo': first_line[4],
            'Codgigo unico do arquivo': first_line[5]
        }]

        next(lista)

        # trata o restante
        self.logging.info('Writting Json')
        with open('arquivo_parseado.json', 'w') as write_file:

            for linha in lista:

                if len(linha) > 2:
                    data = [{
                        'Tipo de Registro': linha[0],
                        'Codigo da Venda': linha[1],
                        'Codigo da Adquirente': linha[2],
                        'Codigo do Estabelecimento': linha[3],
                        'PDV': linha[4],
                        'Codigo da Bandeira': linha[5],
                        'Tipo da Transacao': linha[6],
                        'Valor Total da Venda': linha[7],
                        'Valor Pago': linha[8],
                        'Taxa da Venda': linha[9],
                        'Taxa Total da Venda': linha[10],
                        'Total de Parcelas': linha[11],
                        'Numero do Comprovante': linha[12],
                        'Codigo da Autorizacao': linha[13],
                        'Numero do Resumo': linha[14],
                        'Numero do Cartao': linha[15],
                        'Data da Venda': linha[16],
                        'Hora da Transacao': linha[17],
                        'Codigo do Cliente': linha[18],
                    }]
                    data_dict = data_dict + data

            json.dump(data_dict, write_file, indent=3)
            self.logging.info('Finished')
            print('finish')


if __name__ == '__main__':
    Data()
