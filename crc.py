divisor=list(map(int,input("enter the divisor").split(",")))
divident=list(map(int,input("enter the divident").split(",")))
n=[]
for i in range(0,len(divisor)):
    n.append(divident[0])
    divident.remove(divident[0])
length=len(divisor)

while True:
    print("\n\n")
    if len(divident)==0:
        print("remainder=",m)
        break
    m=[]
    print("upper=",n)
    print("divisor=",divisor)
    for i in range(0,length):
        m.append(n[0]^divisor[i])
        n.remove(n[0])    
    print("xor values=",m)
    delimiter=0
    for i in range(0,length):
        if m[i]!=0:
            delimiter=i
            break
    n=[]    
    for i in range(delimiter,length):
        n.append(m[i])
    difference=length-len(n)
    
    for i in range(0,difference):
        n.append(divident[0])
        divident.remove(divident[0])
    print("new upper values with carries =",n)
    
    
        
        


    
        
    
