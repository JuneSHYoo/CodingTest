# BJ 1703 생장점 <수학, 구현>
# https://www.acmicpc.net/problem/1703
# 시간 : 68ms
# 문제 리뷰 : E, P
# 회고 :

while 1:
    li = list(map(int, input().split()))
    
    if li[0] == 0:
        break

    leaf = 1
    for i in range(len(li)//2):
        leaf = li[1::2][i] * leaf - li[0::2][i+1]
    print(leaf)