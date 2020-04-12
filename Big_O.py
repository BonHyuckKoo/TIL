a = 5 ; b = 6 ; c = 10 
# Constant 가 3개 이므로 => 3

for i in range(n):
    for j in range(n):
        x = i * i  # n^2 =>for 문 중첩
        y = j * j  # n^2 =>for 문 중첩
        z = i * j  # n^2 =>for 문 중첩 => 3n^2
for k in range(n):
    w = a * k + 45 # n = for문 한번(n번만큼 돈다)
    v = b * b      # n = for문 한번(n번만큼 돈다) => 2n
d = 33
# Constant 가 1개 이므로 =>  1

# 총 T(n) = 3 + 3n^2 + 2n + 1 
# T(n) = 4 + 3n^2 + 2n (최고차항은 n^2)
# Big-O 로 표현시 => O(n^2) 
           