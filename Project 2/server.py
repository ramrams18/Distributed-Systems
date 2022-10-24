from xmlrpc.server import SimpleXMLRPCServer
from random import randint
import multiprocessing
from time import sleep
from threading import Thread
from xmlrpc.client import ServerProxy

ports = [8000, 8001, 8002, 8003]
# setting the vector clock values for all to zero intial stages
vector_clock = [0]*len(ports)
port = 0


def vector_clock_increment():
    # in this method we increment vector clock for all the ports when we receive a message from client for the required port
    global vector_clock
    global port
    port_index = ports.index(port)
    vector_clock[port_index] += 1
    return


def vector_clock_update(vector):
    # here we update the clock with the previous version and compare and check with other version
    global vector_clock
    # here we are using the vector method using zip so we can compare and add the max values
    vector_clock_list = zip(vector, vector_clock)
    vector_clock_sample = []
    for i, j in vector_clock_list:
        # here we append the max value out of 2
        vector_clock_sample.append(max(i, j))
    vector_clock = vector_clock_sample
    return


def get_message(vector):
    global port
    res = ""  # here we get a message from differnet client to update
    res = res + "Vector clock before receiving the message " + \
        str(port) + ": " + str(vector_clock) + "\n"
    vector_clock_increment()
    vector_clock_update(vector)
    res = res + "Vector clock after receiving the message " + \
        str(port) + ": " + str(vector_clock) + "\n"
    return res


def recieve_msg(recv_port):
    global port, vector_clock
    res = ""  # here we recieve a message from differnet client to update
    res = res + "Vector clock before sending the message for port, " + \
        str(port) + ": " + str(vector_clock) + "\n"
    vector_clock_increment()
    res = res + "Updated vector clock for port no" + \
        str(port) + " is : " + str(vector_clock) + "\n"
    prox = ServerProxy("http://localhost:" + str(recv_port))
    out_msg = prox.get_message(vector_clock)
    res = res + out_msg + "Node on port no " + \
        str(port) + " sent a message" + "\n"

    return res


def server_run(uport):
    global port
    port = uport  # register all the functions of the server
    server = SimpleXMLRPCServer(('localhost', port), allow_none=True)
    server.register_introspection_functions()
    server.register_function(get_message)
    server.register_function(recieve_msg)
    print("Server is running on this port " + str(port))
    server.serve_forever()
    return


def nodes(ports):
    print("Server has started")
    # this we use the concept for multi processing pool and parallely process
    with multiprocessing.Pool(processes=len(ports)) as pool:
        pool.map(server_run, [x for x in ports])
    return


def main():
    try:
        thread = Thread(target=nodes, args=(ports,))
        thread.start()
        sleep(3)
    except Exception as e:
        print('Exception ', e)


if __name__ == '__main__':
    main()
