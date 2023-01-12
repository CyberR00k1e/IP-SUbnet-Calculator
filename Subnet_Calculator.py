import math
import re
cidr = "10.10.31.22/25"
new= cidr.split("/")
octets1=new[0]
octets2=octets1.split(".")
print(octets2)

class_A= re.search("10.*.*,*",new[0])
class_B=re.search("(^172\.1[6-9]\.)|(^172\.2[0-9]\.)|(^172\.3[0-1]\.)", new[0])
class_C=re.search("192.168.*.*", new[0])

if class_A:
    block=8
elif class_B:
    block=16
elif class_C:
    block=24
subnets= int(new[1])-block
hosts= 32-int(new[1])
print(hosts, subnets)
#test=new[1]/8 !=0 then div = test.split(".") and power = new[1]-(8*div), z2^power is th
octet_used1=int(new[1])/8
print(octet_used1)
if octet_used1 !=0:
    octet_used2=str(octet_used1)
    final_octet= octet_used2.split(".")
    power1=int(final_octet[0])
    print(power1)
    power2=int(new[1])-(8*power1)
print(power2)

power3=8-power2

network=math.pow(2,power3)
network=int(network)
print(network)

if class_B:
    octet_B=[]

    for i in range(power1-1):
        octet_B.append(octets2[i])

    IP = ".".join(octet_B)
    print(IP)

    print(f"The network block size is {network}; range is {IP}.{network}.0 - {IP}.{network}.255 ")

if class_A:
    octet_A=[]

    for i in range(power1-1):
        octet_A.append(octets2[i])

    IP = ".".join(octet_A)
    print(IP)

    print(f"The network block size is {network}; range is {IP}.{network}.0 - {IP}.{network}.255 ")

if class_C:
    octet_C=[]

    for i in range(power1-1):
        octet_C.append(octets2[i])

    IP = ".".join(octet_C)
    print(IP)

    print(f"The network block size is {network}; range is {IP}.{network}.0 - {IP}.{network}.255 ")
