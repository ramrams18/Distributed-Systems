import os
from xmlrpc.server import SimpleXMLRPCServer
from pathlib import Path
rpc_server = SimpleXMLRPCServer(("localhost", 8080), allow_none=True)
print("Listening on port 8080")


def upload(message, filecontent):
    print(message)
    print(filecontent)
    c_workingdirectory = os.getcwd()
    path = os.path.join(c_workingdirectory, 'uploads')
    if not os.path.isdir(path):
        os.mkdir(path)
    path = os.path.join(path, message)
    with open(path, 'w') as f:
        f.write(filecontent)


def delete(message):
    # here we are deleting from  the uploads folder where we will store the file.
    c_workingdirectory = os.getcwd()
    path = os.path.join(c_workingdirectory, 'uploads')
    file_path = os.path.join(path, message)
    if os.path.isfile(file_path):
        os.remove(file_path)


def download(message):
    c_workingdirectory = os.getcwd()
    path = os.path.join(c_workingdirectory, 'uploads')
    file_path = os.path.join(path, message)
    file_path = Path(file_path)
    file_data = (file_path.read_bytes()).decode("utf-8")
    return file_data


def rename_file(oldfilename, newfilename):
    c_workingdirectory = os.getcwd()
    path = os.path.join(c_workingdirectory, 'uploads')
    file = os.path.join(path, oldfilename)
    print(file)
    new_file = os.path.join(path, newfilename)
    print(new_file)
    os.rename(file, new_file)


rpc_server.register_function(upload, 'upload')
rpc_server.register_function(download, 'download')
rpc_server.register_function(rename_file, 'rename_file')
rpc_server.register_function(delete, 'delete')
rpc_server.serve_forever()
