T = 1
sie = []
K, N, M = 3,10,5

map = [1,0,1,0,1,0,1,0,0,1,0,0]


choong = [1,3,5,7,9,10]

count = 0
buspoint = 0

for i in range(0,len(choong)-1):
    sie.append(abs(choong[i] - choong[i + 1]))

for filt in sie:
    if filt > K:
        print("응안되")

while True:

    for cos in range(len(choong)-1, -1 ,-1):

        

        if choong[cos] -buspoint > K:
            continue

        if choong[cos] -buspoint <= K:
            buspoint = choong[cos]
           
            if buspoint == 10:
            
                break

            print(buspoint)
            count +=1
            break


    if buspoint == 10:
        break
       
print(sie)   
print(count)     