# Imports
import csv
import os
import time


# Return a list of strings, each a message
def getListOfMessages():
    # Get the absolute location of this file
    dir_path = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(dir_path)
    msg_list = []
    if 'messages.csv' in files:
        with open(dir_path + '/messages.csv', 'r') as msgfile:
            msg_reader = csv.reader(msgfile, delimiter=';')
            for row in msg_reader:
                msg_list.append(row)
    return msg_list


# Handle incoming message from the webpage
def addMessage(message):
    # Get the absolute location of this file
    dir_path = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(dir_path)
    with open(dir_path + '/messages.csv', 'a+') as msgfile:
        msg_writer = csv.writer(msgfile, delimiter=';')
        msg_writer.writerow([str(time.time()), message, 'unknown'])

    
# If this file is directly called:
if __name__ == '__main__':
    print(getListOfMessages())
