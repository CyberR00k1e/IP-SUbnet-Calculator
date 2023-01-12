'''

10.10.10.22/18
32-18= 14 (hosts)
18-8 = 10 (subnets)

255.255.?.*

? above has 2 bits taken for subnet so, 6 bit for hosts 2^6 is 64,
so 64 onwards is the host

take input

identify class A/B/C

look at the cidr and then find the octet and hosy many host bit


'''
import math
import re
cidr = "10.10.10.18/29"
new= cidr.split("/")

class_A= re.search("10.*.*,*",new[0])
class_B=re.search("172.16.*.*", new[0])
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
test=int(new[1])/8
print(test)
if test !=0:
    test=str(test)
    div = test.split(".")
    power1=int(div[0])
    print(power1)
    power2=int(new[1])-(8*power1)
print(power2)

power3=8-power2

network=math.pow(2,power3)
print(network)

