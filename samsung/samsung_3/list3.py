from collections import Counter

T = int(input())

for i in range(1,T + 1):
    N = int(input())
    a = list(map(int,input()))

    list1 = []
    list2 = []
    list3 = []

    for x in range(0,10):
        list1.append([x,a.count(x)])
        list2.append(a.count(x))


    for y in range(0,10):
        if list1[y][1] == max(list2):
            list3.append(y)

    print("#{0} {1} {2}".format(i,max(list3),max(list2)))
       

    
    
    
       

   
    
    
        

