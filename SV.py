from socket import *
from threading import Thread
s = socket(AF_INET, SOCK_DGRAM)  # UDP Connection

s.bind(("127.0.0.1", 1234))

print("\nUDP Chat Server Running on Port 1234\n")

c, addr = s.recvfrom(1024)



def Send_Massage():
    while True:
        msg = input("You=> ")
        s.sendto(msg.encode(),addr)



def Recieve_Massage():
    while True:
        data = s.recv(1024)
        print("recv=> "+data.decode())
if __name__ == '__main__':
    Thread(target= Send_Massage()).start()
    Thread(target= Recieve_Massage()).start()

s.close()
