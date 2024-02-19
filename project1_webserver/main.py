from socket import * # import socket module

import sys  # In order to terminate the program

# Project 1- Webserver
# By: Jeffrey Wong

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a server socket
# Fill in 1 start
serverPort = 5678
serverSocket.bind(('', serverPort))
serverSocket.listen(1) # Identifies that the server will accept only one connection
# Fill in 1 end

while True:
    # Establish the connection
    print('Ready to serve...')
    # Fill in 2
    connectionSocket, addr = serverSocket.accept()

    try:
        # Fill in 3
        message = connectionSocket.recv(4096).decode()

        filename = message.split()[1]
        f = open(filename[1:]) # Open for reading by default
        # Fill in 4
        outputdata = f.read() # Reads contents of file

        # Send one HTTP header line into socket
        # Fill in 5 start
        messageheader = "HTTP/1.1 200 OK\r\n\r\n"
        connectionSocket.send(messageheader.encode()) # Need to send header
        # Fill in 5 end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in 6 start
        notfoundmessage = "HTTP/1.1 404 Not Found\r\n\r\nCouldn't find file\r\n"
        connectionSocket.send(notfoundmessage.encode())

        # Fill in 6 end

        # Close client socket
        # Fill in 7 start
        connectionSocket.close()
        break # Exit from while loop
        # Fill in 7 end

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data