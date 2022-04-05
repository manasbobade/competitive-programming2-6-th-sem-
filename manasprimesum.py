#   MANAS ANILRAO BOBADE   ROLL NO-39    TY-CSE(A)  CP-2
from itertools import combinations
number=int(input("enter the number"))
list_of_primes=[]
def checkprime(num):
    if num==2:
        return True
    for i in range(2,num):
        if num%i==0:
            return  False
    return True
for i in range(2,number+1):
    if checkprime(i):
        list_of_primes.append(i)
print("list of primes=",list_of_primes)

a=combinations(list_of_primes,4)
b=[]
for i in a:
    b.append(list(i))
for i in b:
    if i[0]+i[1]+i[2]+i[3]==number:
        print("\n\nsum of 4 primes for number=",number," is---",i[0]," ",i[1]," ",i[2]," ",i[3],"=",i[0]+i[1]+i[2]+i[3])
        break
