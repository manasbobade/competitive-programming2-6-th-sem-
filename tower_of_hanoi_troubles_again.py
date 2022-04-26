a=int(input("enter number of pegs"))
b=int(input("enter number of balls"))
count_list=[]
square_list=[]
for i in range(0,a):
    count_list.append([0])
for i in range(1,b+1):
    square_list.append(i**2)
for i in range(1,b+1):
    if i==1:
        count_list[0].append(i)
        continue
    for j in count_list:
        boolean=False
        if i+j[-1] in square_list:
            j.append(i)
            boolean=True
            break
    if boolean==False:
        for m in count_list:
            if m[-1]==0:
                m.append(i)
                break
count=1
for i in count_list:
    i.remove(0)
for i in count_list:
    print("peg number=",count," and elements =",i)
    count+=1
    

    
