import pyfiglet
import sys
import socket
from datetime import datetime
  
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)
  
# Defining a target
if len(sys.argv) == 2:
     
    #Domain name to ip
    target = socket.gethostbyname(sys.argv[1]) 
else:
    print("Invalid amount of Argument")
 

print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)
  
try:
     
    # Scans for open ports ranging from 1 to 65535
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
         
        # returns an error indicator
        result = s.connect_ex((target,port))
        if result ==0:
            print("Port {} is open".format(port))
        s.close()
         
except KeyboardInterrupt:
        print("\n EXITING SCANNER !!")
        sys.exit()
except socket.gaierror:
        print("\n HOSTNAME NOT RESOLVED !!")
        sys.exit()
except socket.error:
        print("\n !! SERVER NOT RESPONDING !!")
        sys.exit()