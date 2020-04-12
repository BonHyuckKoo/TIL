N = 2
purple = "p"
count = 0
paper = [[0] * 10 for i in range(10)]

for i in range(N):
    r1 ,c1, r2, c2 ,color = map(int,input().split(" "))
    if color == 1:
        color= "r"
    else:
        color = "b"

    for y in range(c2 - c1 , c2 + 1):
        if "r" in paper[y][r1:r2+1] or "b" in paper[y][r1:r2+1]:
            for x in paper[y][r1:r2+1]:
                if x != color and x != 0 and x != purple:
                    count += 1                              
        else:
            paper[y][r1:r2+1] = [color] * (c2 - c1 + 1)



print(count)    
