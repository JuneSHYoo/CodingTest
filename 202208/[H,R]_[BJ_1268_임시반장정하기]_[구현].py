import sys
n = int(sys.stdin.readline())

cnt = [[0]*5]*n
std = [[*map(int, sys.stdin.readline().split())] for _ in range(n)]

print(cnt)
print(std)

for col in range(5):
    for i in range(n):
        for j in range(i+1,n, 1):
            if std[i][col] == std[j][col]:
                cnt[i][col] = 1
                cnt[j][col] = 1

for i in range(n):
    cnt[i] = sum(cnt[i])
print(cnt.index(max(cnt))+1)