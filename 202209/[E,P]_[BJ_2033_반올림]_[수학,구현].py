# BJ 2033 반올림 <수학, 구현>
# https://www.acmicpc.net/problem/2033
# 시간 : 72 ms
# 문제 리뷰 : E, P
# 회고 : round 함수 - 5를 반올림 할땐 올림이 아닌 가장 가까운 짝수로 반환한다.

n = int(input())

for i in range(1,len(str(n))):
    if str(n)[-i] == '5':
        n = (int(str(n)[:-i]) + 1) * 10**i
    else:
        n = round(n, -i)
print(n)