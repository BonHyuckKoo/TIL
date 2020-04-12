
def prime(a):
    if a <= 1:
        return False

    i = 2
    while i*i <=a:
        if a % i ==0:
            return False

        i += 1
    return True

while True:
    count = 0
    A = int(input())
    if A == 0:
        break
    
    for i in range(A , A*2 +1):
        if prime(i):
            count +=1
    print(count)                        