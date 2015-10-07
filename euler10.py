import math

def testPrime(num):
    for testPrime in range (2,int(math.sqrt(num))+1):
        if num%testPrime==0:
            return False
    return True        
    
N=2000000
cptPrime=0;
num=2
while num<=N:
    if testPrime(num):
        cptPrime+=num
    num+=1
print(cptPrime)
