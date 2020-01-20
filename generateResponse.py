#!/bin/python3

# Imports
import os
from messageHandler import *
import gmusic.gmusic
from threading import Thread


# This script generates index.html and returns it as a string of bytes

html_head = (b'HTTP/1.1 200 OK\r\n'
                 b'Content-Type: text/html;\r\n'
                 b'\r\n')
css_head = (b'HTTP/1.1 200 OK\r\n'
                 b'Content-Type: text/css;\r\n'
                 b'\r\n')

extension_list = ['html', 'ico', 'css']




# what to do with the requested file
def handleRequest(requested_file):

    # Main page
    if requested_file == 'index.html' or requested_file == '':
        response = html_head + genIndex()

    # Message page
    elif requested_file == 'messages.html':
        response = html_head + genMessages()

    # Music control page
    elif requested_file == 'music.html':
        response = html_head + genMusic()
    
    # Receiving a message
    elif requested_file[0:4] == 'MES_':
        addMessage(requested_file[4:len(requested_file)])
        response = html_head + genMessages()

    elif requested_file[0:4] == 'MUS_':
        decodeMusic(requested_file[4:len(requested_file)])
        response = html_head + genMusic()
        
    # any files in the html folder
    elif requested_file in os.listdir('html'):
        # Check the file extension
        dot_pos = requested_file.rfind('.')
        extension = requested_file[dot_pos+1 : len(requested_file)]
        
        # .html, .ico
        if extension in extension_list[0:2]:
            response = html_head
            # .css
        elif extension == extension_list[2]:
            response = css_head
        # Send 404 if file extension not in list
        else:
            requested_file = '404.html'
            response = html_head
        
        response += convertToBinary('html/' + requested_file)
              
        
    # Send 404 for all other things
    else:
        response = convertToBinary('html/404.html')

    return response




'''
--- HELPER FUNCTIONS ---
'''

# Generate the index page
def genIndex():
    html = ( convertToBinary('html/head.html') +
             convertToBinary('html/index-body.html') +
             convertToBinary('html/tail.html') )
    return html


# Generate the music page
def genMusic():
    html = ( convertToBinary('html/head.html') +
             convertToBinary('html/music-body.html') +
             convertToBinary('html/tail.html') )
    return html


# Generate the message page
def genMessages():
    html = ( convertToBinary('html/head.html') +
             genMsgList() +
             convertToBinary('html/tail.html') )
    return html


# Returns byte string of messages in html syntax
def genMsgList():
    full_msg = b'<p><p>'
    msg_list = getListOfMessages()
    for msg in msg_list:
        full_msg += bytes(('<p>' + str(msg[1]) + '</p>'), 'utf8')
    full_msg += b'<p><p>'
    return full_msg


# Convert given file to binary
def convertToBinary(file):
    with open(file, 'rb') as bfile:
        return bfile.read()


# Decode the message from the music page
def decodeMusic(message):
    if message == 'revplaylist':
        # Run the gmusic script in another thread
        thread = Thread(target=gmusic.gmusic.reverseplaylist, args = ('',True,))
        thread.start()
        
