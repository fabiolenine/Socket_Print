# coding=utf-8
from socketIO_client import SocketIO
import win32print

defprt = win32print.GetDefaultPrinter()

print 'SequenceSocket iniciado...'

def ouvindoPrint(*args):
    vdic = args[0]

    vservico = (vdic['servico']['titulo']).encode('utf-8')
    vatendimento = vdic['atendimento'].encode('utf-8')
    vsequencia = vdic['sequence'].encode('utf-8')
    vtimestamp = vdic['timestamp'].encode('utf-8')

    print 'iniciando a impressao...'

    print vservico
    print 'Atendimento: ' + vatendimento
    print 'Sequencia: ' + vsequencia
    print 'Chegou as: ' + vtimestamp

    # Impressão
    prt = win32print.OpenPrinter(defprt)
    win32print.StartDocPrinter(prt, 1, (vsequencia, None, None))
    try:
        win32print.WritePrinter(prt, '========================================' + "\r\n")
        win32print.WritePrinter(prt, '        Cartorio Moreira de Deus' + "\r\n")
        win32print.WritePrinter(prt, '========================================' + "\r\n")
        win32print.WritePrinter(prt, 'Servico: ' + "\r\n")
        win32print.WritePrinter(prt, vservico + "\r\n")
        win32print.WritePrinter(prt, '----------------------------------------' + "\r\n")
        win32print.WritePrinter(prt, 'Atendimento: ' + vatendimento + "\r\n")
        win32print.WritePrinter(prt, 'Sequencia: ' + vsequencia + "\r\n")
        win32print.WritePrinter(prt, 'Chegou as: ' + vtimestamp + "\r\n")
        win32print.WritePrinter(prt, '----------------------------------------' + "\r\n")
        win32print.WritePrinter(prt, 'A sequencia sera chamada 3 vezes, caso' + "\r\n")
        win32print.WritePrinter(prt, 'nao compareca ao balcão tera que' + "\r\n")
        win32print.WritePrinter(prt, 'solicitar outra sequencia.' + "\r\n")
        win32print.WritePrinter(prt, '========================================' + "\r\n\f")
    finally:
        win32print.EndDocPrinter(prt)
    win32print.ClosePrinter(prt)

# Conexão
socketIO = SocketIO('10.1.1.4', 8080)
socketIO.on('print', ouvindoPrint)
socketIO.wait()