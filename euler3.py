import math

def testPrime(num):
    for testPrime in range (2,int(math.sqrt(num))+1):
        if num%testPrime==0:
            return False
    return True


N=600851475143
num=int(N/2)
while num>2:
    if testPrime(num) and N%num==0:
        break
    num-=1
print(num)
