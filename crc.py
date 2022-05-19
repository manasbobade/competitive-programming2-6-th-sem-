l=[1,0,1,0,0,0,0,1,0,0,0]
a=[0,0,0,1,0,0,0]
b=[1,0,0,1]
n=[1,0,1,0]
length=len(b)
while True:
    print("\n\n")
    if len(a)==0:
        print("remainder=",m)
        break
    m=[]
    print("upper=",n)
    print("lower=",b)
    for i in range(0,length):
        m.append(n[0]^b[i])
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
        n.append(a[0])
        a.remove(a[0])
    print("new upper values with carries =",n)
    
    
        
        


    
        
    
