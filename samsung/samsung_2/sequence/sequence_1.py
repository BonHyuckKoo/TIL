st1 = (90,80)
st2 = (85,75)
st3 = (90,100)

st = list()
st.append(st1)
st.append(st2)
st.append(st3)

for i in range(0,len(st)):
    total = 0
    total = st[i][0] + st[i][1] 
    print("{0}번 학생의 총점은 {1}점이고, 평균은 {2:0.1f}입니다.".format(i + 1,total,total/len(st[0])))
