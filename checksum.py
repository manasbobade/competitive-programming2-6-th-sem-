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
print(a,listofnumbers)
for i in listofnumbers:
    bin1=""
    for j in i:
        bin_value= "{0:04b}".format(int(j, 16))
        bin1+=bin_value
    binarylist.append(bin1)
print(binarylist)        
