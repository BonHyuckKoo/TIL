data_list = []


def int_input():
    total = 0
    for i in range(1,6):
        a = int(input("{0}번째 숫자:".format(i)))
        data_list.append(a)
        total += a
    return total      

print(int_input()/len(data_list))
print(data_list)

score = 0
average = [i/len(data_list) for i in data_list score += i]



