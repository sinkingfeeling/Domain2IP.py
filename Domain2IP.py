import sys
import socket

ip_address = sys.argv[1]
try:
    hostname = socket.gethostbyaddr(ip_address)[0]
    print("Hostname: ", hostname)
except socket.herror as e:
    print("Error: ", e)
