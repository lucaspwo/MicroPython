from socket import *


serverName = ''   # ip do servidor (em branco)
serverPort = 23035 # porta a se conectar
serverSocket = socket(AF_INET, SOCK_STREAM)   # criacao do socket TCP
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #Faz o reuso da porta e do endereco
serverSocket.bind((serverName, serverPort))   # bind do ip do servidor com a porta
serverSocket.listen(1)  # socket pronto para "ouvir" conexoes
connectionSocket, addr = serverSocket.accept()

msg = connectionSocket.recv(1024)
print(msg.decode("utf-8"))

connectionSocket.send('1'.encode())
connectionSocket.close()
