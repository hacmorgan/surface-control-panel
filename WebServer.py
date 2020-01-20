#!/bin/python3

# Imports
import socket
import sys
import os
import argparse
from generateResponse import *

# Argument parsing for port number
parser = argparse.ArgumentParser(description='Port number')
parser.add_argument('port', type=int, nargs='?', default=8080, help='The port number to use if necessary')
args = parser.parse_args()
port = args.port


# create TCP socket and listen on that socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = ('localhost', port)
sock.bind(server)
sock.listen(1)


while True:
    
    # waiting for connection
    connection, client_address = sock.accept()

    try:
        data = str(connection.recv(1024))

        # Extract the file requested
        requested_file = data[data.find('GET')+5:data.find('HTTP')-1]
        print (requested_file)
        
        # Handle the request 
        response = handleRequest(requested_file)

        # Send the response
        connection.sendall(response)
        
 
    finally:
        connection.close()

