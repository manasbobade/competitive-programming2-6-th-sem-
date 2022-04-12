#39 MANAS BOBADE 
import math
from itertools import combinations
#number_list=list(map(int,input("enter the numbers").split(" ")))
#number_list=[3, 4, 5, -3, 100, 1, 89, 54, 23, 20]
number_list=[23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4]
length=len(number_list)
original_sum=sum(number_list)
sum_list=[math.ceil(original_sum/2),math.floor(original_sum/2)]
sum_list=list(set(sum_list))
print(sum_list)
if length%2==0:
    a=combinations(number_list,int(length/2))
    for i in a:
        i=list(i)
        list1=[]
        list2=[]
        for j in number_list:
            if j in i:
                list1.append(j)
                i.remove(j)
            else:
                list2.append(j)
        sum1=sum(list1)
        sum2=sum(list2)
        if sum1 in sum_list and sum2 in sum_list:
            if sum1+sum2==original_sum:
                print("side one =",list1," side 2= ",list2,"\n sum of each side=",sum1," ",sum2)
else:
    a=combinations(number_list,int(length/2))
    for i in a:
        i=list(i)
        list1=[]
        list2=[]
        for j in number_list:
            if j in i:
                list1.append(j)
                i.remove(j)
            else:
                list2.append(j)
        sum1=sum(list1)
        sum2=sum(list2)
        if sum1 in sum_list and sum2 in sum_list:
            if sum1+sum2==original_sum:
                print("side one =",list1," side 2= ",list2,"\n sum of each side=",sum1," ",sum2)
    a=combinations(number_list,math.ceil(length/2))
    for i in a:
        i=list(i)
        list1=[]
        list2=[]
        for j in number_list:
            if j in i:
                list1.append(j)
                i.remove(j)
            else:
                list2.append(j)
        sum1=sum(list1)
        sum2=sum(list2)
        if sum1 in sum_list and sum2 in sum_list:
            if sum1+sum2==original_sum:
                print("side one =",list1," side 2= ",list2,"\n sum of each side=",sum1," ",sum2)  
