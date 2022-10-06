from xmlrpc import client
import threading
from threading import Thread
from time import sleep
from xmlrpc.client import ServerProxy

proxy = ServerProxy("http://localhost:8080", allow_none=True)


def main():
    thread = threading.Thread(target=client)
    thread.start()
# https://docs.python.org/3/library/xmlrpc.client.html


def client():
    while True:
        proxy.file_sync()
        sleep(10)
        print("sync files for every 10 seconds")


if __name__ == '__main__':
    main()
