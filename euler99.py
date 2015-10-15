ns={}
f=open('p099_base_exp.txt','r')
for l in f:
    a=list(map(int,l.split(",")))
    print(l)
    ns[pow(a[0], a[1])]=a

maxVal=0
maxCpt=0
cpt=1
for key in ns:
    if key>maxVal:
        maxVal=key
        maxCpt=cpt
    cpt+=1
print(cpt)
