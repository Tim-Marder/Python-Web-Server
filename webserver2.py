# import socket module
from socket import *

# In order to terminate the program
import sys
import threading

# Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM)
### YOUR CODE HERE ###
serverPort = 6789
serverSocket.bind( ("", serverPort) )
serverSocket.listen(1)

def proc(connectionSocket):
    # Establish the connection
    try:
        message = connectionSocket.recv(1024)

        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()

        # Send one HTTP header line into socket
        outputdata = 'HTTP/1.1 200 OK\r\n\r\n' + outputdata

        # Send the content of the requested file into socket
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        #connectionSocket.send("\r\n".encode())
        print("200 OK")
        # Close client socket
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        outputdata = 'HTTP/1.1 404 Not Found\r\n\r\n'

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        print("404 Not Found")
        # Close client socket
        connectionSocket.close()

#Threading
while True:
    print('Ready to serve...')

    connectionSocket, addr = serverSocket.accept()

    thread = threading.Thread(target = proc, args = (connectionSocket,))
    thread.start()

# Close server socket
serverSocket.close()

# Terminate the program after sending the corresponding data
sys.exit()

