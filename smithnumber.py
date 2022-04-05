number=int(input("enter the number"))
list_of_primes=[]
factors=[]
sum=0
sum_of_digits=0
for i in str(number):
    sum_of_digits+=int(i)
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
        
for i in list_of_primes:
    while True:
        if number%i==0:
            factors.append(i)
            number=number/i
        else:
            break
for i in factors:
    sum+=i
    
print("factors=",factors," sum of factors=",sum," sum of digits=",sum_of_digits)    
