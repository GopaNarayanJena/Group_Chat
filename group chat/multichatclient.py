import socket
import select
import sys

Host="localhost"
Port=5000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
name=raw_input("enter name: ")
s.connect((Host,Port))
s.send(name)
server=s.recv(1024)
print server,' is online....'
sys.stdout.write('[Me] ');
sys.stdout.flush()
data=' '
while data!='exit':
    ready_to_read,_,_=select.select([sys.stdin,s],[],[])
    for read in ready_to_read:
        if read is s:
            data=s.recv(1024)
            print "\r",data
            data=data.split("] ",2)
            data=data[1]
        else:
            data=raw_input()
            dat="[" + name + "] " + data
            s.send(str(dat))
        if data!='exit':
            sys.stdout.write('[Me] ');
            sys.stdout.flush()
s.close()
sys.exit()
