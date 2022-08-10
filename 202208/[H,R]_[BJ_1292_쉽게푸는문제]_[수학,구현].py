# BJ 1292 쉽게 푸는 문제 <수학,구현>
# https://www.acmicpc.net/problem/1292
# 시간 : 76 ms
# 문제 리뷰 : H , R
# 회고 : 1,2,2,3,3,3,4,4,... 수열 만드는 법  

a,b = map(int, input().split())
arr =[0]

for i in range(50):
    for j in range(i):
        arr.append(i)

print(sum(arr[a:b+1]))
