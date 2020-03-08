# random 모듈함수로 로또번호 만들기
import random

def input_start():
    strat  = 0
    try:
        start = int(input("로또 번호의 시작 번호를 입력하세요(기본값:1):"))
    except:
        start = 1
    finally:
        return start

def input_stop():
    stop  = 0
    try:
        stop = int(input("로또 번호의 끝 번호를 입력하세요(기본값:45):"))
    except:
        stop = 45
    finally:
        return stop

def input_count():
    count  = 0
    try:
        count = int(input("로또 공의 개수를 입력하세요(기본값:6):"))
    except:
        count = 6
    finally:
        return count

def print_lotto(start,stop,count):
    lotto = random.sample(range(start, stop+1 , 1),count)
    print("행운의 로또 번호는 ",end="")
    for i, num in enumerate(sorted(lotto)):
        if i == len(lotto) - 1:
            print("{0} ".format(num), end="")
        else:
            print("{0}, ".format(num), end="")
    print("입니다.")

print_lotto(1,45,6)