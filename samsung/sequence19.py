a = list(input().split(","))
b = []
for x in a:
    b.append(x.strip())

b.sort()    


for i in b: 
    if i == b[-1]:
        print(i)
    else:
        print(i, end =", ")
       
    
     