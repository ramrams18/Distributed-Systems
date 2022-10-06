from xmlrpc.server import SimpleXMLRPCServer


def addition(val1, val2):
    return val1 + val2


def sorting(num):
    num.sort()
    return num


rpc_server = SimpleXMLRPCServer(("localhost", 8080))
print("Listening on port 8080")
rpc_server.register_function(sorting, 'sorting')
rpc_server.register_function(addition, 'addition')
rpc_server.serve_forever()
