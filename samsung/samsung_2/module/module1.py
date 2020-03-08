## import

import math 
print(math.radians(90))
print("math.radians(90) = {0}".format(math.radians(90)))
print(math.ceil(3))
print("math.ceil(3.2) = {0}".format(math.ceil(3.2)))
print("math.floor(3.2) = {0}".format(math.floor(3.2)))

print("math.pi = {0}".format(math.pi))

## import ~ as ~
print("-" * 30 + "import ~ as~")

import math as m
print(m.radians(90))
print("m.radians(90) = {0}".format(m.radians(90)))
print(m.ceil(3))
print("m.ceil(3.2) = {0}".format(m.ceil(3.2)))
print("m.floor(3.2) = {0}".format(m.floor(3.2)))

print("m.pi = {0}".format(m.pi))

# from ~ import ~
print("-" * 30 + "from ~ import ~")

from math import radians, ceil, floor ,pi

print(radians(90))
print("radians(90) = {0}".format(radians(90)))
print(ceil(3))
print("ceil(3.2) = {0}".format(ceil(3.2)))
print("floor(3.2) = {0}".format(floor(3.2)))
print("pi = {0}".format(pi))


## sys 모듈
print("-" * 30 + "sys 모듈")
import sys

print("sys.argv => {0} {1}".format(type(sys.argv), sys.argv))
  # sys.argv: 리스트 타입, 명령행에서 python 명령에 전달된 인자들의 정보를 담고있음

for i, val in enumerate(sys.argv): # Enumerate 객체로 변환 및 반복실시
    print("sys.argv[{0}] => {1}".format(i, val))

## random 모듈
print("-" * 30 + "random 모듈")
from random import random, uniform, randrange, choice, choices, sample, shuffle

#random()
print("random() => {0}".format(random()))
#uniform(,)
print("uniform({0}, {1}) => {2}".format(1.0, 10.0, uniform(1.0, 10.0)))

#randrange(,,)
start, stop, step = 1, 45, 2
print("randrange({0}, {1}) => {2}".format(start, stop ,randrange(start, stop)))
print("randrange({0}) => {1}".format(stop, randrange(stop)))
print("randrange({0}, {1}, {2}) => {3}".format(start, stop, step, randrange(start, stop, step)))

#choice() , choices(,) , sample(,) , shuffle()
data_list = list(range(1,6))
print("choice({0}) => {1}".format(data_list, choice(data_list)))
print("choices({0}) => {1}".format(data_list, choices(data_list, k=2)))
print("sample({0}) => {1}".format(data_list, sample(data_list, k=2)))

shuffle(data_list)
print("data_list => {0}".format(data_list))

### datetime 모듈
print("-" * 30 + "datetime 모듈")

from datetime import datetime, timezone, timedelta

now = datetime.now() # 현재 지역의 날짜와 시각 정보를 가진 datatime 객체를 얻음
print("{0}-{1:02}-{2:02} {3:02}:{4:02}:{5:02}".format(now.year, now.month, now.day, now.hour,  now.minute, now.second))
    #{1:02} 여기서 02 는 앞에붙을 0의 개수
print(now.year,now.month, now.day, now.hour,  now.minute, now.second)
print(now)

fmt = "%Y{0} %m{1} %d{2} %H{3} %M{4} %S{5}"
print(now.strftime(fmt).format(*"년월일시분초"))
