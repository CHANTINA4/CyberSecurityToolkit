import socket
domain = input("Enter the Domain Name: ").strip()
port = int(input("Enter port: "))
if len(domain) == 0:
    print("Enter the Domain Name here!!")
else:
    try:
        ip_address = socket.gethostbyname(domain)

        scanner = socket.socket()
        result = scanner.connect_ex((ip_address,port))
        if result == 0:
            print("Port is OPEN")
        else:
            print("Port is closed")
        scanner.close()
    except socket.gaierror:
        print("Invalid Domain Name")