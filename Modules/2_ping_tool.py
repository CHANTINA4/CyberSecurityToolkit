import subprocess
target = input("Enter IP address and Domain: ").strip()
# TODO: Run ping command 
if len(target) == 0:
    print("❌ Please enter an IP address or domain.")
else:
    # print("Running Ping.......")
    result = subprocess.run(
        ["ping", target],
        capture_output = True,  #output screen pr mt chhodo mujhe dedo
        text = True             #taaki output Binary me na aae text aae
    )
    print(result.returncode)
    print(result.stdout)
    if result.returncode == 0:         # Professional way me hum returncode use krte h
        print("Host is UP")
    else:
        print("Host is Down")