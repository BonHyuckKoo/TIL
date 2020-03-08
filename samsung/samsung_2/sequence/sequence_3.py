result = []

for x in range(2,10):
    a = [i * x for i in range(1,10)]  
       
    result.append(list(filter(lambda x : x % 3 != 0 and x % 7 != 0,a)))  
    a = []

print(result)