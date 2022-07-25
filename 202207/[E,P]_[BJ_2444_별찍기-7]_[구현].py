# BJ 2444 별 찍기 -7 <구현>
# https://www.acmicpc.net/problem/2444
# 시간 : 72 ms
# 문제 리뷰 : E , P
# 회고 : 

n = int(input())
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1))
for i in range(n-1, 0, -1) :
    print(" "*(n-i) + "*"*(2*i-1))
    
    
'''
Best Answer
n=int(input())
for i in range(-n+1,n):i=abs(i);print(' '*i+'*'*((n-i)*2-1))
'''