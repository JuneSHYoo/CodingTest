# BJ 1598 꼬리를 무는 숫자 나열 <수학, 사칙연산>
# https://www.acmicpc.net/problem/1598
# 시간 : 68ms
# 문제 리뷰 : E, P
# 회고 :

x,y = map(int, input().split())
x -= 1
y -= 1
print( abs(x//4- y//4) + abs(x%4 - y%4))
