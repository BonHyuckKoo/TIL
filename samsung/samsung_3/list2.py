T = int(input())

for case in range(1,T + 1):
     
     K, N, M = map(int,input().split(" "))
     choong = list(map(int,input().split(" ")))
     choong.append(N)
     count = 0
     buspoint = 0
     sie = []
     bp = 0

     for i in range(0,len(choong)-1):
          sie.append(abs(choong[i] - choong[i + 1]))

     for filt in sie:
          if filt > K:               
               print("#{0} {1}".format(case, count))
               bp = 1
               break

     if bp == 1 : 
          continue

     while True:       
          for cos in range(len(choong)-1, -1 ,-1):                    
               if choong[cos] -buspoint > K:                    
                    continue

               if choong[cos] -buspoint <= K:                   
                    buspoint = choong[cos]          
                    if buspoint == N:
                         break         
                    count +=1
                    break

          if buspoint == N:
               break
               
     print("#{0} {1}".format(case,count))         
