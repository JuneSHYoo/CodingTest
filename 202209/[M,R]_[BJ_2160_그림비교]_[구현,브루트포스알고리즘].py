# BJ 2160 그림비교 <구현,브루트포스알고리즘>
# https://www.acmicpc.net/problem/2160
# 시간 : 76 ms
# 문제 리뷰 : M, R
# 회고 :

n = int(input())
pic = []
mini = 36
ans1 = ans2 = 0

for i in range(n):
    row = []
    for _ in range(5):
        row.append(input())
        
    pic.append(row)

for pic1 in range(n):
    for pic2 in range(pic1 + 1, n):
        cnt = 0
        for r in range(5):
            for c in range(7):
                if pic[pic1][r][c] != pic[pic2][r][c]:
                    cnt += 1
        if mini > cnt :
            mini = cnt
            ans1 = pic1
            ans2 = pic2 
            
print(f'{ans1 + 1} {ans2 +1}')