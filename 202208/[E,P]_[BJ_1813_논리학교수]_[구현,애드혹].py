# BJ 1813 논리학 교수 <구현,애드혹>
# https://www.acmicpc.net/problem/1813
# 시간 : 80 ms
# 문제 리뷰 : E , P
# 회고 :

import sys
n = int(sys.stdin.readline())
*a, = map(int, sys.stdin.readline().split())
cnt = 0

for i in a:
    if i == a.count(i) and i > cnt:
        cnt = i

print(-1 if (a.count(0) > 0) and (cnt == 0) else cnt)