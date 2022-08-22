# BJ 1551 수열의 변화 <수학,구현,문자열,시뮬레이션,파싱>
# https://www.acmicpc.net/problem/1551
# 시간 : 72 ms
# 문제 리뷰 : E , R
# 회고 : 리스트의 요소만 출력할 때 print(*a, sep='구분인자') 사용

n,k = map(int, input().split())
*a, = map(int, input().split(','))

for i in range(k):
    for i in range(len(a) -1):
        a[i] = a[i+1] - a[i]
    a = a[:-1]

print(*a, sep=',')