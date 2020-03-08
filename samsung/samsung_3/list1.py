list1 = []
T = int(input())

for i in range(T):
     N = int(input())
     a = list(map(int,input().split(" ")))
     list1.append(max(a) - min(a))
      
    
     
for i in range(T):
     print("#{0} {1}".format(i + 1,list1[i]))