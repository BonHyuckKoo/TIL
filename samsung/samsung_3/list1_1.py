from random import randrange

T = int(input())

list2 = []

for i in range(0,T):
    list1 = []
    N = int(input())

    for i in range(0,N):
        a = randrange(1,1000000)
        print(a, end = " ")
        list1.append(a)
    
    print()
    list2.append(max(list1) - min(list1))
    
for i in range(1,T + 1):
    print("#{0} {1}".format(i,list2[i - 1]))       


