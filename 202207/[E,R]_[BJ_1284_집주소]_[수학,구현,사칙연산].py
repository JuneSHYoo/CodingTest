# BJ 1284 집 주소 <수학, 구현, 사칙연산>
# https://www.acmicpc.net/problem/1284
# 시간 : 72ms
# 문제 리뷰 : E, R
# 회고 : 주요 연산자의 시간 복잡도를 고려해서 더 간결하게 풀어보는 연습.

def total(n):
    s = 0 
    for i in range(len(n)):
        if n[i] == '0':
            s += 4
        elif n[i] == '1':
            s += 2
        else:
            s += 3

    return len(n)+1+ s

while 1:
    n = input()
    if n== '0' :
        break
    print(total(n))

'''
Best Answer
while 1:
    n = input()
    if n == '0':
        break
    print( len(n)*4+1-n.count('1')+n.count('0'))
'''