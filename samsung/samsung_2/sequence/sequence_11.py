def fibo(x):
    if x <= 2:
        return 1
    return fibo(x-1) + fibo(x-2)

result = [fibo(i) for i in range(1,11)]

print(result)

