import socket
domain = input("Enter the domain name: ").strip()
if len(domain) == 0:
    print("❌Please ente a domain name")
else:
    try:
        ip_address = socket.gethostbyname(domain)
        print("IP Address:", ip_address)
    except socket.gaierror:
        print("Domain not found")
