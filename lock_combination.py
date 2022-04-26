list_of_numbers=[0,1,2,3,4,5,6,7,8,9]
original=list(map(int,input("enter the original state of the lock").split(",")))
print(original)
to_get=list(map(int,input("enter the desired state of the lock").split(",")))
print(to_get)
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
print(forward)     
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
print(backward)
for i in range(0,len(original)):
    a=forward[i]
    b=backward[i]
    print(min(a,b))
    #min_steps.append(min(a,b))
print(min_steps)    
