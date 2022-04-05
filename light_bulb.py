no_of_bulbs=int(input("enter number of bulbs"))
no_of_rounds=int(input("enter number of rounds"))
to_check=int(input("enter the bulb number to check"))
count=0
dict1={0:"off",1:"on"}
for i in range(1,no_of_rounds+1):
    if to_check%i==0:
        count+=1
print("the status of bulb number ",to_check," is ",dict1[count%2])
