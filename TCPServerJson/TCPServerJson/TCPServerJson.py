from socket import *
import threading
import json
import random

def handleClient(connectionSocket, addr):
    while True:
        inputRecieved = connectionSocket.recv(1024).decode()
        jsonText = json.loads(inputRecieved)
        operationInput = jsonText["Operation"]
        num1 = int(jsonText["Number1"])
        num2 = int(jsonText["Number2"])
        sendResult = ""
        if operationInput != "Random" and operationInput != "Add" and operationInput != "Subtract":
            sendResult = operationInput + "unknown operation"
        if operationInput == "Random":
            if num1 > num2:
                sendResult = "Error: Number 2 must be higher than Number 1, when choosing Random"
            elif num1 == num2:
                sendResult = "Error: Number 1 and Number 2 cannot be the same, when choosing Random"
            elif num1 == str:
                sendResult = "Error: Number 1 must consist of numbers and not letters"
            elif num2 == str:
                sendResult = "Error: Number 2 must consist of numbers and not letters"
            elif num2 > num1:
                sendResult = json.dumps(random.randint(num1,num2))
        if operationInput == "Add":
            if num1 == str:
                sendResult = "Error: Number 1 must consist of numbers and not letters"
            elif num2 == str:
                sendResult = "Error: Number 2 must consist of numbers and not letters"
            sendResult = num1 + num2
        if operationInput == "Subtract":
            if num1 == str:
                sendResult = "Error: Number 1 must consist of numbers and not letters"
            if num2 == str:
                sendResult = "Error: Number 2 must consist of numbers and not letters"
            sendResult = num1 - num2
        jsonResult = json.dumps(sendResult)
        connectionSocket.send(jsonResult.encode())

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient,args=(connectionSocket, addr)).start()