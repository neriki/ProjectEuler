import math

def testPrime(num):
    if num==2:
        return True
    if num%2==0:
        return False
    for testPrime in range (2,int(math.sqrt(num))+1):
        if num%testPrime==0:
            return False
    return True


N=600851475143
num=int(N/2)+1
while num>2:
    if testPrime(num) and N%num==0:
        break
    num-=1
print(num)
