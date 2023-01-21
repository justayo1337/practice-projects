#!/usr/bin/env python3
import socket as soc
import struct
import binascii

#setup socket for windows
#s = soc.socket(soc.AF_INET,soc.SOCK_RAW,soc.IPPROTO_IP)
s = soc.socket(soc.PF_PACKET,soc.SOCK_RAW,soc.ntohs(0x0800))

#s.bind(("172.28.66.16",1337))
#s.setsockopt(soc.IPPROTO_IP, soc.IP_HDRINCL,1)
#s.ioctl(soc.SIO_RCVALL, soc.RCVALL_ON)

def eth_header(data):
	storeobj = data
	storeobj = struct.unpack("!6s6sH",storeobj)
	dest_mac=binascii.hexlify(storeobj[0])
	src_mac = binascii.hexlify(storeobj[1])

	eth_protocol=storeobj[2]
	data={"Destination Mac":dest_mac, "Source Mac":src_mac,"Protocol":eth_protocol}
	return data
def ip_header(data):
	
	storeobj = struct.unpack("!BBHH",data)
	ver = storeobj[0]
	IHL =storeobj[1]
	TOS = storeobj[2]
	length = storeobj[3]

	stuff = { "Version": ver, "IHL": IHL, "TOS": TOS, "Len": length}
	return stuff	
while True:
    print("Waiting on packetssss...........")
    pkts = s.recvfrom(65565)
    #print(pkts)
    print(eth_header(pkts[0][0:14]))
    print(ip_header(pkts[0][14:20]))
