a = list(map(int,input().split(",")))



for i in a: 
    if i == a[-1] and i % 2 == 1:
        print(i)
    elif i % 2 ==1:
        print(i, end =", ")
       