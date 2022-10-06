from xmlrpc.client import ServerProxy
import os
from pathlib import Path
proxy = ServerProxy("http://localhost:8080", allow_none=True)


def main():
    operation = input(
        "Enter operation upload//delete//download//rename ").lower()
    filename = input("please enter file name for operation ")
    if operation == "upload":
        file = Path(filename)
        if not file.is_file():
            print('File not exists')
        else:
            file_data = (file.read_bytes()).decode("utf-8")
            proxy.upload(filename, file_data)
            print("File is uploaded")

    elif operation == 'delete':
        proxy.delete(filename)
        print("File is deleted")

    elif operation == 'download':
        data = proxy.download(filename)
        c_workingdirectory = os.getcwd()
        path = os.path.join(c_workingdirectory, 'downloads')
        if not os.path.isdir(path):
            os.mkdir(path)
        else:
            path = os.path.join(path, filename)
            with open(path, 'w') as f:
                f.write(data)
        print("File is downloaded")

    elif operation == "rename":
        new_filename = input("Enter new filename for file to be changed ")
        print(filename, new_filename)
        proxy.rename_file(filename, new_filename)
        print("file is renamed")


if __name__ == '__main__':
    main()
