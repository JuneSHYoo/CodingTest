# BJ 2442 별 찍기 -5 <구현>
# https://www.acmicpc.net/problem/2442
# 시간 : 68ms
# 문제 리뷰 : E , R
# 회고 : 최대한 한줄에 별을 다 찍을 수 있도록!

import sys
n = int(sys.stdin.readline())
for i in range(1,n+1):
    print(" "*(n-i) + "*"*(2*i-1))