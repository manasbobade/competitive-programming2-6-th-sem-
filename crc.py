a=[1,0,1,0,0,0,0,1,0,0,0]
b=[1,0,0,1]
length=len(b)
m=[]
count=0
while True:
    for i in range(0,length):
        m.append(a[i])
        a[i]=5
        count+=1
    for i in range(0,4):
        m[i]=int(m[i])^int(b[i])
    for i in range(0,4):
        if m[i]==1:
            break
        else:
            m[i]=5
    j=[]
    for i in m:
        if i==5:
            continue
        j.append(i)
    m.clear()    
    for i in j:
        m.append(i)
    j.clear()    
    print(m)
    diff=4-len(m)
    
    break
        


    
        
    
