# BJ 2455 지능형 기차 <수학,구현, 사칙연산>
# https://www.acmicpc.net/problem/2455
# 시간 : 68 ms
# 문제 리뷰 : E , P
# 회고 : 

total_pop = 0
max_pop = 0 

for i in range(4):
    x,y = map(int, input().split(' '))
    total_pop -= x 
    total_pop += y
    if total_pop > max_pop: max_pop = total_pop
print(max_pop)