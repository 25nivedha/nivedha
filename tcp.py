from socket import * 
server_ip="10.1.24.125"
server_port=6789
server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.bind((server_ip,server_port))
server_socket.listen(1)
print("welcome:the server is now ready to receive")
connection_socket,address=server_socket.accept()
while True:
  sentence=connection_socket.recv(2048).decode()
  print('>>',sentence)
  Message=input(">>")
  connection_socket.send(Message.encode())
  if(Message=='q'):
   connectionsocket.close()
