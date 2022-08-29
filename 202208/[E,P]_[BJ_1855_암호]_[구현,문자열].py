# BJ 1855 암호 <구현,문자열>
# https://www.acmicpc.net/problem/1855
# 시간 : 72 ms
# 문제 리뷰 : E , P
# 회고 :

n = int(input())
let = input()

orig = []
for i in range(int(len(let) / n)):
    if i % 2 == 0 :
        orig.append(list(let[n*i:n*(i+1)]))
    if i % 2 == 1:
        orig.append(list(let[n*i:n*(i+1)])[::-1])

ans = ''
for i in range(n):
    for l in orig:
        ans += l[i]
        
print(ans)