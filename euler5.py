def test(n,v):
    for i in range(2,v+1):
        if n%i != 0:
            return True
    return False


val=20
n=val
while test(n,val):
    n+=1
print(n)
