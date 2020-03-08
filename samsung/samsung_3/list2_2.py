T = 1
sie = []
K, N, M = 3,10,5

choong = [1,3,5,7,9]
choongpoint = [0] * (N + 1)

for i in choong:
    choongpoint[i] = 1


for i in range(0,len(choong)-1):
    sie.append(abs(choong[i] - choong[i + 1]))

for filt in sie:
    if filt > K:
        print("응안되")

print(choongpoint)        