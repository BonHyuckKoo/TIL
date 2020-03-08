###################### 리스트 ####################

a = "안녕하세요"
b = "100" # 정수형은 분해가 안됨

data_list1 = list(a)
data_list2 = list(b)

print(data_list1)
print(data_list2)


## 리스트 항목 접근
print("-"*30+"리스트 항목 접근")

data_list = [10,20,30,40,50]

print("data_list[0] => {0}".format(data_list[0]))
print("data_list[1] => {0}".format(data_list[1]))
print("data_list[2] => {0}".format(data_list[2]))
print("data_list[3] => {0}".format(data_list[3]))
print("data_list[4] => {0}".format(data_list[4]))

print("data_list[-5] => {0}".format(data_list[-5])) #data_list[0]과 같음
print("data_list[-4] => {0}".format(data_list[-4]))
print("data_list[-3] => {0}".format(data_list[-3]))
print("data_list[-2] => {0}".format(data_list[-2]))
print("data_list[-1] => {0}".format(data_list[-1]))

print("data_list[0:3] => {0}".format(data_list[0:3]))
print("data_list[-5:-2] => {0}".format(data_list[-5:-2]))

print("data_list.index(20) => {0}".format(data_list.index(20)))


## 리스트 기본연산
print("-"*30+"리스트 기본 연산")

data_list1, data_list2 = [10,20,30] , [40,50]

print("{0} + {1} => {2}\n".format(data_list1,data_list2,data_list1 + data_list2))
print("{0} * 2 => {1}".format(data_list1,data_list1 *2))
print("{0} * 3 => {1}\n".format(data_list2,data_list2 *3))


print(id(data_list1))
print("data_list1: {0} {1}".format(hex(id(data_list1)),data_list1))
       #  data_list1 의 객체주소를 16진수로 표현
print("data_list1: {0} {1}".format(hex(id(data_list2)),data_list2))

## 리스트 항목 추가
print("-"*30+"리스트 항목 추가")
data_list = [10,20,30,40]

print("data_list: {0}".format(data_list))
 
     # .append(추가할값) 
data_list.append(50) # 반환 값:None
data_list.append(60)
print("data_list: {0}".format(data_list))

    # .insert(추가할곳(인덱스), 추가할값)
data_list.insert(2,25)
print("data_list:{0}".format(data_list))

    # extend (리스트 마지막에 추가할값들<= 리스트만 됨)
   
data_list.extend([70, 80])   
data_list.append([90, 100])
print("data_list: {0}".format(data_list))   


## 리스트 항목 변경
print("-"*30+"리스트 항목 변경")

data_list = [10,20,30,40]

data_list[2] = 29 # 2 인덱스에 있는값을 29로
print("data_list: {0}".format(data_list)) #[10,20,30,40]

data_list[1:3] = [12, 15] # [1:3] 슬라이싱 된곳을 12, 15로
print("data_list: {0}".format(data_list)) # [10,12,15,40]

data_list[1:3] = [12, 15, 20, 30] # [1:3] 슬라이싱 된곳을 12, 15 ,20으로(넣을값의 개수가 슬라이싱된 것보다 많아도 됨)
print("data_list: {0}".format(data_list)) # [10,12,15,20,30,40]

data_list[2:3] = [31, 25] # [2:3] 슬라이싱 된곳(즉 인덱스2)을 31, 25로
print("data_list: {0}".format(data_list)) # [10,12,31,25,25,30,40]

## 리스트 항목 제거
print("-"*30+"리스트 항목 제거")

data_list = [10,20,30,40,50,60,70,80,90,100]
   # del 리스트이름[인덱스]
del data_list[2]  # 인덱스 2 에 잇는 값을 삭제
print("data_list: {0}".format(data_list)) 

del data_list[3:5]  # 인덱스 [3:5] 에 잇는 값을 삭제
print("data_list: {0}".format(data_list)) 

   # .pop(인덱스)
data_list.pop(5)
print("data_list: {0}".format(data_list)) 

   # .remove(지울 값)
data_list.remove(100)
print("data_list: {0}".format(data_list)) 

  #.clear(리스트 전부삭제) == del data_list[:] 와 같음
data_list.clear()
print("data_list: {0}".format(data_list)) 

## 리스트 항목 확인
print("-"*30+"리스트 항목 확인")

data_list = [10,20,30,50,50,50,60,70,80]
   #값 in 리스트이름 : 들어잇는지를 True/False로 반환
   #값 not in 리스트이름 : 안들어 있는지를 True/False로 반환
print("50 in data_list => {0}".format(50 in data_list))
print("50 not in data_list => {0}".format(50 not in data_list))

   #리스트이름.count(값) : 값이 리스트에 몇개 들어있는지를 반환
print("data_list.count(50) => {0}".format(data_list.count(50)))
print("data_list.count(55) => {0}".format(data_list.count(55)))

## 리스트와 for 문
print("-"*30+"리스트와 for 문")

data_list = list(range(0, 11, 2))

for item in data_list:
    print("{0}".format(item), end=" ")   # 공백문자로 구분 가로출력

print() # => 이게 없으면 다음 출력과 붙어서 나옴

for idx, item in enumerate(data_list):
    # 인덱스와 항목 정보를 매 반복마다 변수 idx  와 item 에 저장
    print("data_list[{0}] => {1}".format(idx, item))


### 리스트 내포
print("-"*30+"리스트 내포 + 조건")

data_list1 = [1,2,3,4,5]

print("data_list1: {0} {1}".format(type(data_list1),data_list1))

data_list2 = []
for item in data_list1:
    data_list2.append(item)
print("data_list2: {0} {1}".format(type(data_list2),data_list2)) 

data_list3 = [item for item in data_list1] # 리스트 내포하는법
print("data_list3: {0} {1}".format(type(data_list3), data_list3))

data_list4 = []
for item in data_list1:
    if item % 2 ==1:
        data_list4.append(item)
print("data_list4: {0} {1}".format(type(data_list4), data_list4))   

data_list5 = [item for item in data_list1 if item % 2 == 1] #리스트 내포+조건
print("data_list5: {0} {1}".format(type(data_list5), data_list5))

data_list6 = [item for item in data_list1 if item % 2 == 0]
print("data_list6: {0} {1}".format(type(data_list6), data_list6))

data_list7 = []
for x in data_list1:           # for문으로 x 항목 1,3,5 도출
    if x % 2 == 1:             
        for y in data_list1:   # 중첩 for문으로 y 항목 2,4 도출
            if y % 2 == 0:
                data_list7.append(x * y)  #홀수항목 x와 짝수 항목 y와의 곱셈
print("data_list7: {0} {1}".format(type(data_list7), data_list7))    
   # 1*2 ,1*4 , 3*2 , 3*4 ,5*2 ,5*4 
           
data_list8 = [x *y for x in data_list1 if x % 2 ==1 for y in data_list1 if y % 2 ==0]
print("data_list8: {0} {1}".format(type(data_list8), data_list8)) 

data_str = "Hello Python!"
data_list9 = [item.lower() for item in data_str]
print("data_list9: {0} {1}".format(type(data_list9), data_list9)) 


#################   튜플 #################
print("-"*30+"튜플 생성")

data_tuple = (10, 21.5 ,"파이썬", True)
print("{0} {1}".format(type(data_tuple), data_tuple))

data_tuple = tuple(range(10,21,2))
print("{0} {1}".format(type(data_tuple), data_tuple))

data_str = "안녕하세요"
data_tuple = tuple(data_str)
print("{0} {1}".format(type(data_tuple), data_tuple))

## 튜플 항목접근
print("-"*30+"튜플 항목접근")

data_tuple = [10,20,30,40,50]

print("data_tuple: {0}".format(data_tuple))

print("data_tuple[0]: {0}".format(data_tuple[0]))
print("data_tuple[1]: {0}".format(data_tuple[1]))
print("data_tuple[2]: {0}".format(data_tuple[2]))
print("data_tuple[3]: {0}".format(data_tuple[3]))
print("data_tuple[4]: {0}".format(data_tuple[4]))

print("data_tuple[-5]: {0}".format(data_tuple[-5]))
print("data_tuple[-4]: {0}".format(data_tuple[-4]))
print("data_tuple[-3]: {0}".format(data_tuple[-3]))
print("data_tuple[-2]: {0}".format(data_tuple[-2]))
print("data_tuple[-1]: {0}".format(data_tuple[-1]))


print("data_tuple[0:3]: {0}".format(data_tuple[0:3]))
print("data_tuple[-5:-2]: {0}".format(data_tuple[-5:-2]))

print("data_tuple.index(20): {0}".format(data_tuple.index(20)))

## 튜플 기본 연산
print("-"*30+"튜플 기본 연산")

data_tuple1, data_tuple2 = (10,20,30),(40,50)

print("data_tuple1: {0} {1}".format(hex(id(data_tuple1)), data_tuple1))
print("data_tuple1: {0} {1}\n".format(hex(id(data_tuple2)), data_tuple2))

print("{0} + {1} => {2}\n".format(data_tuple1, data_tuple2,data_tuple1+data_tuple2))
print("data_tuple1: {0} {1}".format(hex(id(data_tuple1)), data_tuple1))
print("data_tuple1: {0} {1}\n".format(hex(id(data_tuple2)), data_tuple2))

print("{0} * 2 => {1}".format(data_tuple1, data_tuple1 * 2))
print("{0} * 3 => {1}".format(data_tuple2, data_tuple2 * 3))

## 튜플 항목 확인
print("-"*30+"튜플 항목 확인")

data_tuple = (10,20,30,50,50,50,60,70,80)

print("50 in data_tuple => {0}".format(50 in data_tuple))
print("50 not in data_tuple => {0}".format(50 not in data_tuple))

print("data_tuple.count(50) => {0}".format(data_tuple.count(50)))
print("data_tuple.count(55) => {0}".format(data_tuple.count(55)))

## 튜플과 for 문
print("-"*30+"튜플 과 for 문")

data_tuple = tuple(range(0, 11, 2))

for item in data_tuple:
    print("{0}".format(item), end=" ")

print()

for idx, item in enumerate(data_tuple):
    print("data_tuple[{0}] => {1}".format(idx, item))

 ## 튜플 내포의 특징   
print("-"*30+"튜플 내포의 특징")

data_tuple1 = (1,2,3,4,5)
 
print("data_tuple1: {0} {1}".format(type(data_tuple1),data_tuple1))

data_generator1 = (item for item in data_tuple1)
print("data_generator1: {0} {1}".format(type(data_generator1),data_generator1))

data_tuple2 = tuple(data_generator1)
print("data_tuple2: {0} {1}".format(type(data_tuple2),data_tuple2))

data_tuple3 = tuple(item for item in data_tuple1 if item % 2 ==1)
print("data_tuple3: {0} {1}".format(type(data_tuple3),data_tuple3))

data_tuple4 = tuple(item for item in data_tuple1 if item % 2 ==0)
print("data_tuple4: {0} {1}".format(type(data_tuple4),data_tuple4))

data_tuple5 = tuple(x * y for x in data_tuple1 if x % 2 ==1 for y in data_tuple1 if y % 2 ==0)
print("data_tuple5: {0} {1}".format(type(data_tuple5),data_tuple5))


############ 실습(리스트 객체를 활용해 총점과 평군 구하기)

scores = []
count = int(input("총 학생 수를 입력하세요: "))

for i in range(1, count + 1):
    score = []
    kor = int(input("학생의{0}의 국어 점수를 입력하세요: ".format(i)))
    score.append(kor)
    mat = int(input("학생의{0}의 수학 점수를 입력하세요: ".format(i)))
    score.append(mat)
    eng = int(input("학생의{0}의 영어 점수를 입력하세요: ".format(i)))
    score.append(eng)
    scores.append(score)

for i,score in enumerate(scores):
    total = 0
    for s in score:
        total += s
    print("학생{0}총점: {1}, 평균: {2:0.2f}".format(i + 1,total,total/len(score)))    

    # 95 100 90 /80 85 100 / 70 77 70