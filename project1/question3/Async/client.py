from xmlrpc.client import ServerProxy, Fault
proxy = ServerProxy("http://localhost:8080", allow_none=True)


def main():
    try:
        option = int(input(
            "Choose 1 for addition, 2 for sorting, 3 for result of previous requests "))
        if option == 1:
            print("you chose option 1 for adding 2 numbers")
            number1 = int(input("Enter value 1 "))
            number2 = int(input("Enter value 2 "))
            sum = proxy.addition(number1, number2)
            print("key for acknowledgment: ", sum)
            main()
        elif option == 2:
            n = int(input("enter thenumber of elements to be sorted"))
            array = []
            for i in range(n):
                array.append(int(input("Enter " + str(i+1)+" number ")))
            print("Numbers are: ", array)
            res_array = proxy.sorting(array)
            print("key for acknowledgment: ", res_array)
            main()
        elif option == 3:
            x = input("enter the key value of acknowledgement")
            res = proxy.results(x)
            print("The value of the acknowledgment is ", res)
            main()
        else:
            print("Wrong selection ")
            main()
    except Fault as e:
        print("Fault  code: ", e.faultCode)
        print("Fault String: ", e.faultString)


if __name__ == '__main__':
    main()
