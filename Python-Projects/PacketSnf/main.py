#!/usr/bin/env python3
import socket as soc


#setup socket for windows
#s = soc.socket(soc.AF_INET,soc.SOCK_RAW,soc.IPPROTO_IP)
s = soc.socket(soc.PF_PACKET,soc.SOCK_RAW,soc.ntohs(0x0800))

#s.bind(("172.28.66.16",1337))
#s.setsockopt(soc.IPPROTO_IP, soc.IP_HDRINCL,1)
#s.ioctl(soc.SIO_RCVALL, soc.RCVALL_ON)


while True:
    print("Waiting on packetssss...........")
    print(s.recvfrom(65565))
