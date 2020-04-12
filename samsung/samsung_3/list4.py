T = int(input())
result = []

for i in range(1,T + 1):

    N , M = map(int,input().split(" "))
    v = list(map(int,input().split(" ")))
    list1 = []
    
    for x in range(len(v) - M + 1) :
        score = 0
        for y in range(M):

            if x == len(v) - M:
                score += v[x + y]                    
            else:    
                score += v[x + y] 

        list1.append(score)

    result.append(max(list1) - min(list1))        

    
for i in range(1,len(result) + 1):
    print("#{0} {1}".format(i, result[i - 1]))

    
