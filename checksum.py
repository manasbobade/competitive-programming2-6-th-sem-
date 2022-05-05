#a=input("enter the 16 bit message")
a="012FFA3BC09E45FA"
length=len(a)
lenght_eachline=length/4
listofnumbers=[]
binarylist=[]
count=0
b=""
for i in range(0,length):
    if i==0:
        b=b+a[i]
        count+=1
        continue
    if count==4:
        listofnumbers.append(b)
        b=""
        b=a[i]
        count=1
    else:
        b=b+a[i]
        count+=1
listofnumbers.append(b)    
for i in listofnumbers:
    bin1=""
    for j in i:
        bin_value= "{0:04b}".format(int(j, 16))
        bin1+=bin_value
    binarylist.append(str(bin1))
sum = bin(int(binarylist[0], 2) + int(binarylist[1], 2)+ int(binarylist[2], 2)+ int(binarylist[3], 2))    
sum=str(sum[2:])

if len(sum)>16:
    noofextrabits=len(sum)-16
    extrabits=sum[0:noofextrabits]
    sum=str(sum[noofextrabits:])
    sum=bin(int(sum,2)+int(extrabits,2))
    sum=sum[2:]

if len(sum)<16:
    a=""
    for i in range(0,16-len(sum)):
        a+="0"
sum=str(a+sum)     

ans=[]
count=0
b=""
for i in range(0,len(sum)):
    if i==0:
        b=b+sum[i]
        count+=1
        continue
    if count==4:
        ans.append(hex(int(b,2))[2:])
        b=""
        b=sum[i]
        count=1
    else:
        b=b+sum[i]
        count+=1
ans.append(hex(int(b,2))[2:])
print("checksum=",ans)
    
