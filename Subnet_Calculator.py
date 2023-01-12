import math
import re
#cidr = "10.10.31.22/27"
cidr= input("please enter the private CIDR in IP_Address/subnet format: " ).strip()
new= cidr.split("/")
octets1=new[0]
octets2=octets1.split(".")
#print(octets2)

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
#print(hosts, subnets)
#test=new[1]/8 !=0 then div = test.split(".") and power = new[1]-(8*div), z2^power is th
octet_used1=int(new[1])/8
#print(octet_used1)
#if octet_used1 !=0:
if octet_used1 != 1:

    octet_used2=str(octet_used1)
    final_octet= octet_used2.split(".")
    power1=int(final_octet[0])

    power2=int(new[1])-(8*power1)

    power3 = 8 - power2

    network = math.pow(2, power3)
    network = int(network)
    print(f'''
    ******************************
    Network block size is {network}"
    ******************************''')
    if (int(new[1])>8 and int(new[1])< 16):
            octet_A=[]
            for i in range(1):
                octet_A.append(octets2[i])

            IP = ".".join(octet_A)
            #print(IP)
            print(f"The network blocks are: ")
            for i in range(0,256,network):

                print(f"subnet is {IP}.{i}.0")

    elif (int(new[1])>16 and int(new[1])< 24):
            octet_B=[]
            for i in range(2):

                octet_B.append(octets2[i])
            print(octet_B)

            IP = ".".join(octet_B)

            print(f"The network blocks are: ")

            for i in range(0,256,network):

                print(f"subnet is {IP}.{i}.0")


    elif (int(new[1]) >24 and int(new[1]) < 32):
        octet_C = []
        for i in range(3):
            octet_C.append(octets2[i])
        print(octet_C)

        IP = ".".join(octet_C)

        print(f"The network blocks are: ")
        for i in range(0, 256, network):
            print(f"subnet is {IP}.{i}")

else :

    octet_used1=int(octet_used1)
    octets3=[]
    for i in range(octet_used1):
        octets3.append(octets2[i])
        #print(octets3)
        network = ".".join(octets3)
    if class_A:
        print(f"Subnet is 0; Network is {network}.0.0.0")
    if class_B:
            print(f"Subnet is 0; Network is {network}.0.0")
    if class_C:
        print(f"Subnet is 0; Network is {network}.0")

        #print(IP)

    #print(f"The subnet is 0; the network is {IP}.0.0")





'''
if class_B:
    octet_B=[]

    for i in range(power1):
        octet_B.append(octets2[i])

    IP = ".".join(octet_B)
    print(IP)

    print(f"The network block size is {network}; range is {IP}.{network}.0 - {IP}.{network}.255 ")

if class_A:
    octet_A=[]

    for i in range(power1):
        octet_A.append(octets2[i])

    IP = ".".join(octet_A)
    print(IP)

    print(f"The network block size is {network}; Network address is {IP}.{network}")

if class_C:
    octet_C=[]

    for i in range(power1):
        octet_C.append(octets2[i])

    IP = ".".join(octet_C)
    print(IP)

    print(f"The network block size is {network}; range is {IP}.{network}.0 - {IP}.{network}.255 ")

'''
