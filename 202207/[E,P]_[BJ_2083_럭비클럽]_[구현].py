# BJ 2083 럭비클럽 <구현>
# https://www.acmicpc.net/problem/2083
# 시간 : 72ms
# 문제 리뷰 : E , P
# 회고 : 


while 1:
    x,y,z = input().split()
    if x == '#':
        break
    print(f"{x} Senior" if (int(y) > 17) or (int(z) >= 80) else f"{x} Junior" )