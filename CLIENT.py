
from socket import *
from threading import Thread
s = socket(AF_INET, SOCK_DGRAM) #UDP Connection

s.sendto("Hi ".encode() , ("127.0.0.1",1234))

def Recive_MSG():
    while True:
        data = s.recv(1024)
        print("recv=> "+data.decode())
def Send_MSG():
    while True:
        msg = input("You=> ")
        s.sendto(msg.encode(),("127.0.0.1",1234))




if __name__ == '__main__':
    Thread(target=Recive_MSG()).start()
    Thread(target= Send_MSG()).start()

