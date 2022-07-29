# BJ 2476 주사위 게임 <수학,구현>
# https://www.acmicpc.net/problem/2476
# 시간 : 116 ms
# 문제 리뷰 : E , R
# 회고 : 정렬 순서로 입력받으면 훨씬 풀기 수월해짐

max_p = 0

for i in range(int(input())):
    li = list(map(int, input().split(' ')))

    cnt = []
    for i in range(3):
        cnt.append(li.count(li[i]))

    if max(cnt) == 1:
        price = max(li) * 100
    elif max(cnt) == 2:
        price = 1000+li[cnt.index(2)]*100
    elif max(cnt) == 3:
        price = 10000 + li[cnt.index(3)]*1000
    
    if price > max_p :
        max_p = price

print(max_p)

'''
d=0
for i in range(int(input())):*_,a,b,c=sorted(input());d=max(int(['1'+b,c][a<b<c]+'000'[a<c:]),d)
print(d)
'''