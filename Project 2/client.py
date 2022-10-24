from xmlrpc.client import ServerProxy
from random import choice
from time import sleep

port_nums = [8000, 8001, 8002, 8003]


def checkport_var(port1):
    port2 = choice(port_nums)
    if port2 != port1:  # pick ports on random
        return port2
    else:
        return checkport_var(port1)


def server_call():
    port1 = choice(port_nums)
    # update the next port by random function if we have same port again
    port2 = checkport_var(port1)
    proxy1 = ServerProxy("http://localhost:" + str(port1))
    print("proxy1:", proxy1)
    print("messages started")
    print("Node on port no:" + str(port1) +
          " is sending message to node that is port no: " + str(port2))  # here we send request to client
    res = proxy1.recieve_msg(port2)
    print(res)
    return


def main():

    print("synchronizing all clients")
    for i in range(0, 5):
        server_call()  # we are creating 5 message events to test the vector clock application
        sleep(10)


if __name__ == '__main__':
    main()
