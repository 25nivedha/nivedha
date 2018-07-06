import socket
UDP_IP_ADDRESS="127.0.0.1"
UDP_PORT_NO=6789
message 1=("hai")
bytesTosend = str.encode(message 1)
clientsock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientsock.sendto(bytesTosend,(UDP_IP_ADDRESS,UDP_PORT_NO))
