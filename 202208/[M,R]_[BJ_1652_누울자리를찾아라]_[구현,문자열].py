# BJ 1652 누울 자리를 찾아라 <구현,문자열>
# https://www.acmicpc.net/problem/1652
# 시간 : 76 ms
# 문제 리뷰 : M , R
# 회고 :
n = int(input())
room = [] 

for _ in range(n):
    room.append(list(map(str, input())))
    
res = [0,0]
for i in range(n):
    cnt_h, cnt_v = 0,0
    for j  in range(n):
        if room[i][j] == ".":
            cnt_h += 1
        elif room[i][j] == "X":
            if cnt_h >= 2:
                res[0] += 1
            cnt_h = 0 
        
        if room[j][i] == ".":
            cnt_v += 1
        elif room[j][i] == "X":
            if cnt_v >= 2:
                res[1] += 1
            cnt_v = 0
            
        if j == n-1 :
            if cnt_h >= 2:
                res[0] += 1
            if cnt_v >= 2:
                res[1] += 1

print(' '.join(map(str, res)))


'''
<풀이>
- 누울 자리가 2자리 이상 붙어있으면 누울 자리 1개
- 방을 row별로 room에 저장
- 방을 돌면서 '.'(누울 수 있는 자리) 2개 이상 붙어 있는 곳 탐색
- cnt를 0 으로 초기화 하고 방을 돌면서 '.'발견하면서 cnt 1 증가
- 'X'(벽)을 만났을때 cnt가 2 이상이면 누울 수 있는 자리가 있어서 1 증가
- 방의 마지막이 '.'이고 cnt가 2 이상이면 누울 수 있는 자리에 1을 더해줘야 하기 때문에 j == n-1 로 해결
'''