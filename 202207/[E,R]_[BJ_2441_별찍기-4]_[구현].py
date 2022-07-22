# BJ 2441 별 찍기 -4 <구현>
# https://www.acmicpc.net/problem/2441
# 시간 : 80ms
# 문제 리뷰 : E , R
# 회고 : print할때 end ="" 하면 옆으로 이어서 출력

import sys
n = int(sys.stdin.readline())
for i in range(n):
    for j in range(i):
        print(" ",end ="")
    for j in range(n-i):
        print("*", end = "")
    print('')