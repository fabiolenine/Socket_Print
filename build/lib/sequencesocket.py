# coding=utf-8
from socketIO_client import SocketIO
# import win32print

# defprt = win32print.GetDefaultPrinter()
# prt = wind32print.OpenPrinter(defprt)

print 'SequenceSocket iniciado...'

def ouvindoPrint(*args):
    vdic = args[0]

    vservico = (vdic['servico']['titulo']).encode('utf-8')
    vatendimento = vdic['atendimento'].encode('utf-8')
    vsequencia = vdic['sequence'].encode('utf-8')
    vtimestamp = vdic['timestamp'].encode('utf-8')

    print 'Informação recebida, iniciando a impressão...'

    print '========================================'
    print '        Cartório Moreira de Deus'
    print '========================================'
    print 'Serviço: '
    print vservico
    print '----------------------------------------'
    print 'Atendimento: ' + vatendimento
    print 'Sequência: ' + vsequencia
    print 'Chegou as: ' + vtimestamp
    print '----------------------------------------'

    # Impressão
    # win32print.StartDocPrinter(prt, 1, ("imprimindo sequence", None, None))
    # win32print.WritePrinter(prt, '========================================' + "\r\n" + '\f')  # CRLF+FF
    # win32print.WritePrinter(prt, '        Cartório Moreira de Deus' + "\r\n" + '\f')  # CRLF+FF
    # win32print.WritePrinter(prt, '========================================' + "\r\n" + '\f')  # CRLF+FF
    # win32print.WritePrinter(prt, 'Serviço: ' + "\r\n" + '\f')  # CRLF+FF
    # win32print.WritePrinter(prt, vservico + "\r\n" + '\f')  # CRLF+FF
    # win32print.WritePrinter(prt, '----------------------------------------' + "\r\n" + '\f')  # CRLF+FF
    # win32print.WritePrinter(prt, 'Atendimento: ' + vatendimento + "\r\n" + '\f')  # CRLF+FF
    # win32print.WritePrinter(prt, 'Sequência: ' + vsequencia + "\r\n" + '\f')  # CRLF+FF
    # win32print.WritePrinter(prt, 'Chegou as: ' + vtimestamp + "\r\n" + '\f')  # CRLF+FF
    # win32print.WritePrinter(prt, '----------------------------------------' + "\r\n" + '\f')  # CRLF+FF
    # win32print.EndDocPrinter(prt)
    # win32print.ClosePrinter(prt)

# Conexão
socketIO = SocketIO('192.168.0.6', 8080)
socketIO.on('print', ouvindoPrint)
socketIO.wait()