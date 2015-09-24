f=open('p022_names.txt','r')
cont=f.read().replace('"','')
buff=cont.split(',')
nbWord=len(buff)
sortedBuff=sorted(buff)
score=0
for i in range(0,nbWord):
    word=sortedBuff[i]
    valWord=0
    for c in word:
        valWord+=(ord(c)-ord("A")+1)
    score+=valWord*(sortedBuff.index(word)+1)

print(score)
