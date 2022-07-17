# BJ 1547 공 <구현, 시뮬레이션>
# https://www.acmicpc.net/problem/1547
# 시간 : 68ms
# 문제 리뷰 : E, R
# 회고 : exec() 함수

ball = 1
M = int(input())

for i in range(M):
    x,y = map(int, input().split())
    if ball == x:
        ball = y
    elif ball == y :
        ball = x

print(ball)

'''
Best Answer
a=1;exec'i,j=map(int,raw_input()[::2]);a=[i+j-a,a][i!=a!=j];'*input();print a
'''