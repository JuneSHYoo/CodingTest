# BJ 1267 핸드폰 요금 <구현>
# https://www.acmicpc.net/problem/1267
# 시간 : 68ms
# 문제 리뷰 : E, R
# 회고 : 
'''
input()
c=list(map(int,input().split()))
y,m=0,0
for i in c:y+=(i//30+1)*10;m+=(i//60+1)*15
print(['Y','M'][m<y],*[('M',m),[min(m,y)]][m!=y])
'''

import sys

def cost(x):
    ycost = ((x//30)+1)*10
    mcost = ((x//60)+1)*15
    return ycost, mcost

N = int(sys.stdin.readline())
t = list(map(int, sys.stdin.readline().split()))
y = 0
m = 0
for i in t:
    y += cost(i)[0]
    m += cost(i)[1]
    
if y == m :
    print(f"Y M {y}")
elif y < m :
    print(f"Y {y}")
else:
    print(f"M {m}")
