#Usage:
#python3 scanner.py <ip>

import sys
import socket
from datetime import datetime as dt


if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Change the hostname to IPv4

else:
    print("Invalid arguments were provided.")
    print("Syntax: python3 scanner.py 192.168.10.1")
    sys.exit()


#Opening banner
    print("-" * 50)
    print(f"Scanning target: {target}")
    print(f"Starting at: {dt.now()}") 
    print("-" * 50)


try:
    for port in range(0,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4 and Port
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target,port))
            if result == 0:
                print(f"Port {port} is open")
            else:
                s.close()


except KeyboardInterrupt:
    print("Stopping")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

except socket.error:
    print("Could not connect to server")
    sys.exit()