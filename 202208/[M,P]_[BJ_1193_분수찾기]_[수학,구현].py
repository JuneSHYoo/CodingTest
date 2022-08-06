# BJ 1193 분수찾기 <수학, 구현>
# https://www.acmicpc.net/problem/1193
# 시간 : 68 ms
# 문제 리뷰 : M , P
# 회고 :

n = int(input())
tot = 0
for i in range(1,n+1):
    tot += i
    if tot >= n:
        break
        
u = 1+(tot-n)
d = i-(tot-n)

if i%2 == 1:
    print(f"{u}/{d}")
else:
    print(f"{d}/{u}")