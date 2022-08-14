# BJ 1356 유진수 <수학,구현,문자열,사칙연산>
# https://www.acmicpc.net/problem/1356
# 시간 : 72 ms
# 문제 리뷰 : E , P
# 회고 :

n = input()
answer = 'NO'
for i in range(1,len(n)):
    a = n[0:i]
    b = n[i:len(n)]
    
    l=1 
    r=1
    
    for j in a:
        l*=int(j)
    
    for k in b:
        r*=int(k)
    
    if l == r:
        answer = 'YES'
        break

print(answer)