# BJ 2061 좋은암호 <수학, 브루트포스 알고리즘, 임의 정밀도 / 큰 수 연산>
# https://www.acmicpc.net/problem/2083
# 시간 : 72ms
# 문제 리뷰 : E , P
# 회고 : 


while 1:
    x,y,z = input().split()
    if x == '#':
        break
    print(f"{x} Senior" if (int(y) > 17) or (int(z) >= 80) else f"{x} Junior" )