import socket as soc



s = soc.socket(soc.AF_INET,soc.SOCK_RAW,soc.IPPROTO_IP)
s.bind(("172.12.0.161",1337))
s.setsockopt(soc.IPPROTO_IP, soc.IP_HDRINCL,1)
s.ioctl(soc.SIO_RCVALL, soc.RCVALL_ON)


while True:

    print(s.recvfrom(65565))