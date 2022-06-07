edges=int(input("enter number of edges"))
vertices=int(input("enter number of vertices"))
edges_connections=[]
node_color={}

for i in range(1,vertices+1):
    node_color[i]="Null"
    
print("enter edges in a,b format")
for i in range(0,edges):
    a=list(map(int,input("enter the edge").split(",")))
    edges_connections.append(list(a))
    
flag=True



for i in range(1,vertices+1):
    if flag==False:
        break
    if i==1:
        node_color[i]="blue"
        
    if node_color[i]=="Null":
        for j in edges_connections:
            if i==j[0]:
                if node_color[j[1]]=="Null":
                    continue
                if node_color[j[1]]=="blue":
                    node_color[j[0]]="red"
                elif node_color[j[1]]=="red":
                    node_color[j[0]]="blue"
    else:
        for j in edges_connections:
            if i==j[0]:
                if node_color[j[1]]=="Null":
                    if node_color[j[0]]=="red":
                        node_color[j[1]]="blue"
                    if node_color[j[0]]=="blue":
                        node_color[j[1]]="red"    
                else:
                    if node_color[j[1]]==node_color[i]:
                        print("graph cannot be bicolored")
                        flag=False
                        break          
if flag:
    print("it is a bicolored graph")
    print("node colors are",node_color)
                
            
