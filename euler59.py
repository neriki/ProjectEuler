import string
 
listCorrectChar=list(map(ord ,list(string.ascii_letters + string.digits + " (;:,.'?-!)")))
listCharPass=list(map(ord ,list(string.ascii_lowercase)))
     
def testCharPass(tab, letter):
    uncryptedTab=[x ^ letter for x in tab]
    return not (len(list(set(uncryptedTab + listCorrectChar)))>len(listCorrectChar))
     
def recCharPass(tab):
    for c in listCharPass:
        if testCharPass(tab,c):
            return c
     
listChar1=[]
listChar2=[]
listChar3=[]
f=open('p059_cipher.txt','r')
cont=f.read()
cryptedMess=list(map(int, cont.split(',')))
nb=len(cryptedMess)
for n in range(2,nb,3):
    listChar1.append(cryptedMess[n-2])
    listChar2.append(cryptedMess[n-1])
    listChar3.append(cryptedMess[n])
if n+1<nb:
    listChar1.append(cryptedMess[n+1])
if n+2<nb:    
    listChar2.append(cryptedMess[n+2])
     
CharPass1=recCharPass(listChar1)
CharPass2=recCharPass(listChar2)
CharPass3=recCharPass(listChar3)
       
uncTab1=[x ^ CharPass1 for x in listChar1]
uncTab2=[x ^ CharPass2 for x in listChar2]
uncTab3=[x ^ CharPass3 for x in listChar3]

uncText=''

for i in range(0,len(uncTab1)):
    uncText+=chr(uncTab1[i])
    if i < len(uncTab2):
        uncText+=chr(uncTab2[i])
    if i < len(uncTab3):
        uncText+=chr(uncTab3[i])

print uncText
print(chr(CharPass1)+chr(CharPass2)+chr(CharPass3))
print(sum(uncTab1)+sum(uncTab2)+sum(uncTab3))
