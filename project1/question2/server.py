from re import purge
from xmlrpc.server import SimpleXMLRPCServer
import shutil
import os
import time
from dirsync import sync

server = SimpleXMLRPCServer(('localhost', 8080), allow_none=True)
print("Listening on port 8080...")

client_path = 'C:/Users/dheer/OneDrive/Desktop/Distributed/Assignment 1/question2/client/'
server_path = 'C:/Users/dheer/OneDrive/Desktop/Distributed/Assignment 1/question2/server/'


def file_sync():
    sync(client_path, server_path, 'sync', purge=True)


server.register_function(file_sync, "file_sync")
server.serve_forever()
