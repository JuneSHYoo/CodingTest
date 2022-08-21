# BJ 1546 평균 <수학, 사칙연산>
# https://www.acmicpc.net/problem/1546
# 시간 : 88 ms
# 문제 리뷰 : E , P
# 회고 :

n = int(input())
*score, = map(int, input().split())
print(sum( [i/max(score)*100 for i in score] ) / n)
