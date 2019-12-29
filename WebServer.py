#!/bin/python3

# Imports
import socket
import sys
import argparse
from messageHandler import *
from generateIndex import *

#parser = argparse.ArgumentParser(description='Port number')
#parser.add_argument('port')
#args = parser.parse_args()
port = 8081

#create TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#set port to that used in command
server = ('127.0.0.1', port)
sock.bind(server)
sock.listen(1)

response_head = (b'HTTP/1.1 200 OK\r\n'
                 b'Content-Type: text/html;\r\n'
                 b'\r\n')



while True:
    # waiting for connection
    connection, client_address = sock.accept()

    try:
        print ('Connection from', client_address)
        print ('')
        print ('Data received:')
        print ('')
        data = str(connection.recv(1024))
        print (data)
        requestedFile = data[data.find('GET')+5:data.find('HTTP')-1]
        print (requestedFile)

        # Main page
        if requestedFile == 'index.html' or requestedFile == '':
            response = response_head + genIndex()
            print(response)
            connection.sendall(response)

        # Icon for browser tab
        elif requestedFile == 'favicon.ico':
            imgBinary = convertToBinary(requestedFile)
            response = (response_head + imgBinary)
            connection.sendall(response)

        # Receiving a message
        elif requestedFile[0:4] == 'MES_':
            decodeMessage(requestedFile[4:len(requestedFile)])
            response = response_head + genIndex()
            connection.sendall(response)

                   
        else:
            response = (b'HTTP/1.1 404 Not Found\r\n'
                        b'Content-Type: text/html;\r\n'
                        b'\r\n'
                        b'<html>'
                            b'<head>'
                                b'<title>AAAaaaaAaAAaaaAAaAAaaaA</title>'
                            b'</head>'
                            b'<body bgcolor=white>'
                                b'<p>Thou hath requested something I do not posess!</p>'
                                b'<p>four oh four'
                            b'</body>'
                        b'</html>')
            connection.sendall(response)
        
        
        


    finally:
        connection.close()

