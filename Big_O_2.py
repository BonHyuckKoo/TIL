#### O(n^2) 가 되는 경우 ####

import time
from random import randrange

def findMin(alist):
    overallmin = alist[0]
    for i in alist:          
        issmallest = True
        for j in alist:      #O(N^2) => for 문의 중첩
            if i > j:
                issmallest = False
                break
        if issmallest:
            overallmin = i
    return overallmin

#확인
print(findMin([5,2,1,0]))
print(findMin([0,2,3,4]))

#연산시간
for listSize in range(1000,10001,1000):
    alist = [randrange(100000) for _ in range(listSize)]
    start = time.time()
    print(findMin(alist))
    end = time.time()
    print("size: {}, time: {}".format(listSize, end-start))


