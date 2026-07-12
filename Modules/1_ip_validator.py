ip = input("Enter IP Address: ")
parts = ip.split(".")
if len(parts)!=4:
    print("Invalid IP Address")
else:
    valid = True

    for part in parts:
        if not part.isdigit():
            valid = False
            break
        value = int(part)

        if value < 0 or value >255:
            valid = False
            break
    if valid:
        print("IP valid")
    else:
        print("Not Valid")


