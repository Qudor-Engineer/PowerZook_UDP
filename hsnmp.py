'''
This software developed by: Khudhur Alfarhan (Qudoren@gmail.com)
'''

from hnmp import SNMP
import time
import socket

def hSnmp():

    snmp = SNMP("192.168.1.200", version=1 , community="public")
    current = snmp.get(".1.3.6.1.4.1.19011.1.3.5.1.3.1.0")
    print(current/1000)
    return current/1000


if __name__ == '__main__':

    # UDP_IP = "127.0.0.1"
    UDP_IP = "192.168.1.255"
    UDP_PORT = 5005
    

    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    while True:
        sock.sendto(str(hSnmp()).encode(), (UDP_IP, UDP_PORT))



