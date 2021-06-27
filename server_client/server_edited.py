import socket
import os

s = socket.socket()
s.bind(("localhost", 9995))

s.listen(10)

os.chdir("./server_files")

while True:
    sc, address = s.accept()

    print(address)

    f = open("Recieved_file.csv", 'wb')
    print("Recieved all row")
    l = sc.recv(1024)
    while l:
        f.write(l)
        l = sc.recv(1024)

        if not l:
            break
    f.close()
    sc.close()
    print("Copied FIle")
s.close()
