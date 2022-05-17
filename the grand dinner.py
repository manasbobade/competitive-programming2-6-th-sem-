chairs=4
tables=4
groups=5
group_strength=5

group1=["a","a2","a3","a4","a5"]
group2=["b","b2","b3","b4","b5"]
group3=["c","c2","c3","c4","c5"]
group4=["d","d2","d3","d4","d5"]
group5=["e","e2","e3","e4","e5"]

grouplist=[group1,group2,group3,group4,group5]

table1=[]
table2=[]
table3=[]
table4=[]
table5=[]

tablelist=[table1,table2,table3,table4,table5]
count=0
chairnumber=0
def checktablestrength():
    if len(table1)==len(table2)==len(table3)==len(table4)==len(table5)==4:
        return False
        
def insertintable(j):
    global count
    tablelist[count].append(j)
    count+=1
    count=count%5
        
for i in grouplist:
    if checktablestrength()==False:
        break
    for j in i:
        if checktablestrength()==False:
            break
        insertintable(j)
for i in tablelist:
    print(i)
