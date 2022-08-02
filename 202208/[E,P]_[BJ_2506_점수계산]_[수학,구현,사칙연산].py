# BJ 2506 점수계산 <수학,구현,사칙연산>
# https://www.acmicpc.net/problem/2506
# 시간 : 68 ms
# 문제 리뷰 : E , P
# 회고 : 

n = int(input())
score = list(map(int, input().split()))
e = 1
for i in range(len(score)):
    if score[i] == 1:
        score[i] = e
        e+=1
    else:
        score[i]=0
        e = 1

print(sum(score))