list1 = [[0] * 10 for i in range(10)]



# N = 2

# r1,c1,r2,c2, color = 1,2,3,3,1

# garo1, garo2

# draw = c2 + 1 - c1


# for i in range(0,r2 - r1 + 1):       
                 
#     list1[r1 + i][c1:c2+1] = [color] * draw

# print(list1)
# print(draw)

testCase = int(input())

for case in range(0, testCase):
    # 혹시 모르니 0초기화
    for j in range(0,10):
        for i in range(0,10):
            list1[i][j] = 0
    # 숫자 받기
    numSqure = int(input())
    count = 0
    for k in range(0,numSqure):
        garo1 , sero1 , garo2 ,sero2 ,color = map(int,input().split(" "))

        for insertColor in range(garo1, garo2):
            for insertColor2 in range(sero1, sero2):

                if list1[insertColor][insertColor2] == 3:
                    continue

                if lisert1[insertColor][insertColor2] == color:
                    continue


                list1[insertColor][insertColor2] += color


        
        for garoCheck in range(0, 10):
            for seroCheck in range(0,10):
                if list1[garoCheck][seroCheck] == 3:
                    count = count + 1

    print("#"+case +count)