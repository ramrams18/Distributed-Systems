from xmlrpc.server import SimpleXMLRPCServer
rpc_server = SimpleXMLRPCServer(("localhost", 8080))
print("Listening on port 8080")
result = {}


count1 = 0
count2 = 0


def addition(val1, val2):
    print("here")
    global count1
    count1 += 1
    print(count1)
    result["add "+str(count1)] = val1 + val2
    return "add "+str(count1)


def sorting(num):
    print(num)
    global count2
    count2 += 1
    sort_list = sorted(num)
    result["sort "+str(count2)] = sort_list
    print(result["sort "+str(count2)])
    return "sort "+str(count2)


def results(var):
    return result[var]


rpc_server.register_function(sorting, 'sorting')
rpc_server.register_function(addition, 'addition')
rpc_server.register_function(results, 'results')
rpc_server.serve_forever()
