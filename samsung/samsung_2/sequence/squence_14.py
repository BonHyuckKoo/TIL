dicBase = (('가','깋'), ('나','닣'), ('다','딯'), ('라','맇'), ('마','밓'), ('바','빟'), ('사','싷'),('아','잏'), ('자','짛'), ('차','칳'), ('카','킿'), ('타','팋'), ('파','핗'), ('하','힣'))
inputWord = ['막', '부모님', '비용', '비행기', '원래', '처리', '최초', '꼴', '좀', '들다', '싶다','수출', '계시다', '다', '뒤', '듣다', '함께', '아이', '무척', '보이다', '가지다', '그', '자르다', '데리다', '마리', '개', '정도', '옳다', '놀이','뜨겁다']
result = []
c= []

for i in inputWord:
    for x in range(0,len(dicBase)):
       if dicBase[x][0] <= i  <= dicBase[x][1]:
           c.append(i)

print(result)          
         
        
    