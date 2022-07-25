# BJ 2445 별 찍기 -8 <구현>
# https://www.acmicpc.net/problem/2445
# 시간 : 68 ms
# 문제 리뷰 : E , P
# 회고 : print() 안에 .center를 사용해 지정할 수 있음

n = int(input())
for i in range(-n+1,n): i = abs(i) ;print('*'*(n-i) + ' '*2*i + '*'*(n-i))
'''
Better Answer
n=int(input())
for i in range(-n+1,n):print((' '*abs(2*i)).center(2*n,'*'))
'''