# BJ 2443 별 찍기 -6 <구현>
# https://www.acmicpc.net/problem/2443
# 시간 : 72 ms
# 문제 리뷰 : E , P
# 회고 : 별찍기 -5랑 비슷

n = int(input())
for i in range(n, 0, -1) :
    print(" "*(n-i) + "*"*(2*i-1))