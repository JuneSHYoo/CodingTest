# BJ 1357 뒤집힌 덧셈 <구현, 문자열>
# https://www.acmicpc.net/problem/1357
# 시간 : 72 ms
# 문제 리뷰 : E , P
# 회고 :

x,y = map(str, input().split())
print(int(str( int(x[::-1]) +int(y[::-1]) )[::-1]))