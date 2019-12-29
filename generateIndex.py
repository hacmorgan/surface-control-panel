#!/bin/python3

# Imports
from messageHandler import getListOfMessages


# This script generates index.html and returns it as a string of bytes



index_head = (b'<html>'
              b'<head>'
              b'<title>Welcome to the (crazy) world of Mobeen</title>'
              b'</head>'
              b'<body bgcolor=white>'
              b'<p>This is the home page for your favorite characters Mobeen, Aksa, Eight and Nate</p>'
              b'<p>Curious to see what they look like?</p>'
              b'<a href="MES_penis">test lol </a>')

index_tail = (b'</body>'
              b'</html>')



def convertToBinary(file):
    with open(file, 'rb') as file:
        return file.read()

def genMsgList():
    full_msg = b'<p><p>'
    msg_list = getListOfMessages()
    for msg in msg_list:
        full_msg += bytes(('<p>' + str(msg[1]) + '</p>'), 'utf8')
    full_msg += b'<p><p>'
    return full_msg
        
def genIndex():
    index = index_head + genMsgList() + index_tail
    return index

