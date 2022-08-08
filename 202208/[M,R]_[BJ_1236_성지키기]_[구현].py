# BJ 1236 성 지키기 <구현>
# https://www.acmicpc.net/problem/1236
# 시간 : 72 ms
# 문제 리뷰 : M , R
# 회고 : 전치행렬 구하는 방법 기억해두기 

n,m = map(int,input().split())

cas = []
reverse_cas = ['' for _ in range(m)]
for i in range(n):
    inputs = input()
    cas.append(inputs)
    for idx, inp in enumerate(inputs):
        reverse_cas[idx] += inp 
        
i_cnt = 0
c_cnt = 0 
for idx in range(n):
    if "X" not in cas[idx]:
        i_cnt+=1
for col in range(m):
    if "X" not in reverse_cas[col]:
        c_cnt+=1
print(max(i_cnt, c_cnt))