list_of_numbers=[0,1,2,3,4,5,6,7,8,9]
original=list(map(int,input("enter the original state of the lock").split(",")))
to_get=list(map(int,input("enter the desired state of the lock").split(",")))
min_steps=[]
forward=[]
backward=[]
for i in range(0,len(original)):
    a=original[i]
    b=to_get[i]
    min=0
    count=0
    while True:
        if a==b:
            forward.append(count)
            break
        a=(a+1)%10
        count+=1
for i in range(0,len(original)):
    a=original[i]
    b=to_get[i]
    min=0
    count=0
    while True:
        if a==b:
            backward.append(count)
            break
        a=(a-1)%10
        count+=1
for i in range(0,len(original)):
    m=forward[i]
    n=backward[i]
    if m<n:
        min_steps.append(m)
    else:
        min_steps.append(n)
print("min steps for each combinations are=",min_steps)
total_sum=0
for i in min_steps:
    total_sum+=i
print("total minimun steps=",total_sum)    
    
