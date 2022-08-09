# BJ 1268 임시 반장 정하기 <구현>
# https://www.acmicpc.net/problem/1268
# 시간 : 1384 ms
# 문제 리뷰 : H , R
# 회고 : 

N = int(input())
std = []

for i in range(N):
    std.append([int(j) for j in input().split()])
    
mx_frd = -1
bj = -1

for std_no in range(N):
    result = set()
    for grd in range(5):
        for frd in range(N):
            if std[std_no][grd] == std[frd][grd]:
                result.add(frd)
        if len(result) > mx_frd:
            bj = std_no + 1
            mx_frd = len(result)
print(bj)