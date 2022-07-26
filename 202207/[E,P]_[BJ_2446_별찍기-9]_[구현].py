# BJ 2446 별 찍기 -9 <구현>
# https://www.acmicpc.net/problem/2446
# 시간 : 72 ms
# 문제 리뷰 : E , P
# 회고 : 

n = int(input())
for i in range(1,n+1):
    print(' '*(i-1) + '*' * (2*(n-i)+1))
for j in range(1,n):
    print(' '*(n-j-1) + '*'*((2*j)+1))