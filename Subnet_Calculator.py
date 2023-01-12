
import math
import re
cidr = "172.28.31.22/26"
new= cidr.split("/")

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

