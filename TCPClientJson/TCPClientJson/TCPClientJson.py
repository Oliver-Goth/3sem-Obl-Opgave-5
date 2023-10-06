from socket import *
import json

serverName = 'localhost'
serverPort = 12000
clientSocket  = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while True:
    print('Pick a operation: Random, Add or Subtract:')
    operationInput = input()
    print('Pick number 1:')
    Num1 = input()
    print('Pick number 2')
    Num2 = input()
    
    protocolOptions = {
        "Operation" : operationInput,
        "Number1" : int(Num1),
        "Number2" : int(Num2)
        }
    jsonText = json.dumps(protocolOptions)
    clientSocket.send(jsonText.encode())
    recievedMessage = clientSocket.recv(1024).decode()
    print(json.loads(recievedMessage))