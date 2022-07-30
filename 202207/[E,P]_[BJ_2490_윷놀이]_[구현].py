# BJ 2490 윷놀이 <구현>
# https://www.acmicpc.net/problem/2490
# 시간 : 68 ms
# 문제 리뷰 : E , P
# 회고 : 

for i in range(3): a = list(map(int,input().split(' '))) ; print('A' if (sum(a) == 3) else 'B' if sum(a) == 2 else 'C' if sum(a) == 1 else 'D' if sum(a) == 0 else 'E')