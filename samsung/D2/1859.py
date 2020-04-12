T = int(input())

for case in range(1 , T + 1):

    N = int(input())
    price = list(map(int,input().split(" ")))
    money = 0

    for i in range(0,len(price)):

        if max(price) - price[i] > 0 :
            money += max(price) - price[i]
        elif price[i] == max(price):
            price[i] = 0  
            
    print("#{0} {1}".format(case,money))         