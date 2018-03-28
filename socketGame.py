import socket
import threading

port = 8089
print("Select mode [server | client]:")
mode = input()
connection = None
if mode == "server":
  serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  serversocket.bind(('', port))
  serversocket.listen(1)
  connection, address = serversocket.accept()
elif mode == "client":
  print("Select address [XXX.XXX.XXX.XXX]")
  address = input()
  connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  connection.connect((address, port))
print("CONNECTION IS ACTIVE")
def waitNetwork():
  while True:
    bArray = connection.recv(1000)
    print(bArray.decode())

threading.Thread(target=waitNetwork).start()

while True:
  toSend = input()
  connection.send(toSend.encode())