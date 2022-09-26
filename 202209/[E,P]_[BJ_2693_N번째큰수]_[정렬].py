# BJ 2693 N번째 큰 수 <정렬>
# https://www.acmicpc.net/problem/2693
# 시간 : 152 ms
# 문제 리뷰 : E, P 
# 회고 : 

n = int(input())

for i in range(n):
    *a, = map(int, input().split())
    print(sorted(a)[-3])