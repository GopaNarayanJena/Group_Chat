#cannot handles same names
#if any last two client exit then server will stop automatically
import socket
import select
import sys

Host="localhost"
Port=5000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((Host,Port))
s.listen(1)
print 'ready to accept request'
name="GOOOGLY_SERVER"
socket_list=[[s],[name]]
data=' '
ind=0
cnt=1
while data!='exit':
    ready_to_read,_,_=select.select(socket_list[0],[],[])
    for read in ready_to_read:
        if read == s:
            c, addr = s.accept()
            socket_list[0].append(c)
            cnt=cnt+1
            friend=c.recv(1024)
            socket_list[1].append(friend)
            print "Got new connection from '",friend,"'"
            c.send(name)
        else:
            dat=read.recv(1024)
            data=dat.split("] ",2)
            data=data[1]
            if data=='exit':
                ind=socket_list[0].index(read)
                friend=socket_list[1][ind]
                print socket_list[1][ind]," is offline"
                socket_list[0].remove(read)
                socket_list[1].remove(friend)
                cnt=cnt-1
                if cnt>2:
                    data=" "
                else:
                    for i in range(1,cnt):
                        if read != socket_list[0][i]:
                            socket_list[0][i].send(dat)
            else:
                for i in range(1,cnt):
                    if read != socket_list[0][i]:
                        socket_list[0][i].send(dat)
s.close()
sys.exit()
