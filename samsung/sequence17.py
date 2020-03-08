a = list(map(int,input("숫자 입력: ").split(",")))

pi = 3.141592

for i in a: 
    if i == a[-1]:
        print(round(2*pi*i,2))
    else:
        print(round(2*pi*i,2), end =", ")


  
   
