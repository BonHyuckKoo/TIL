M = int(input())
N = int(input())

numlist = [i for i in range(M,N+1)]
result = []
def isprime(x):
    if x <=1 : 
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False

        i += 1
    return True

for i in numlist:
    if isprime(i):
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))            


