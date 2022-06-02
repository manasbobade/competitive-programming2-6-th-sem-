a=input("enter the ip address").split(".")
m=a[3].split("/")
a.remove(a[3])
a.append(m[0])
#a=[124,156,221,123]
b=[]
    
sizeofnetid=int(m[1])
firstaddress=[]
lastaddress=[]
subnet=[]


for i in a:
    b.append(format(int(i),"08b"))

count=0
for i in b:
    a=""
    for j in i:
        count+=1
        if count>sizeofnetid:
            a+="0"
        else:
            a+="1"
    subnet.append(a)
print("subnet address==",int(subnet[0],2),".",int(subnet[1],2),".",int(subnet[2],2),".",int(subnet[3],2))    

count=0
for i in b:
    a=""
    for j in i:
        count+=1
        if count>sizeofnetid:
            a+="0"
        else:
            a+=str(j)
    firstaddress.append(a)

print("first address==",int(firstaddress[0],2),".",int(firstaddress[1],2),".",int(firstaddress[2],2),".",int(firstaddress[3],2))

count=0
for i in b:
    a=""
    for j in i:
        count+=1
        if count>sizeofnetid:
            a+="1"
        else:
            a+=str(j)
    lastaddress.append(a)

print("last address==",int(lastaddress[0],2),".",int(lastaddress[1],2),".",int(lastaddress[2],2),".",int(lastaddress[3],2))


