a=input("enter the ip address").split(".")

if int(a[0])>=0 and int(a[0])<=127:
    print("class of the given ip address is -A-")
    print("subnet mask=255.0.0.0")
    print("first address=",str(a[0])+".0.0.0")
    print("last address=",str(a[0])+".255.255.255")
    
elif int(a[0])>=128 and int(a[0])<=191:
    print("class of the given ip address is -B-")
    print("subnet mask=255.255.0.0")
    print("first address=",str(a[0])+"."+str(a[1])+".0.0")
    print("last address=",str(a[0])+"."+str(a[1])+".255.255") 
elif int(a[0])>=192 and int(a[0])<=223:
    print("class of the given ip address is -C-")
    print("subnet mask=255.255.255.0")
    print("first address=",str(a[0])+"."+str(a[1])+"."+str(a[2])+".0")
    print("last address=",str(a[0])+"."+str(a[1])+"."+str(a[2])+".255")  
elif int(a[0])>=224 and int(a[0])<=239:
    print("class of the given ip address is -D-")
elif int(a[0])>=240 and int(a[0])<=255:
    print("class of the given ip address is -E-")
else:
    print("invalid ip address entered")
    
    
