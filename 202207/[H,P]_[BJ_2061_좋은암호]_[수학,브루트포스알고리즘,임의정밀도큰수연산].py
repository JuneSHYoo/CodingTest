# BJ 2061 좋은암호 <수학, 브루트포스 알고리즘, 임의 정밀도 / 큰 수 연산>
# https://www.acmicpc.net/problem/2061
# 시간 : 356ms
# 문제 리뷰 : H , P
# 회고 : 백준 1837번이랑 같은 문제 , 에라토스체네스의 체 이용해서 풂

K, L = map(int, input().split())
p = [1]*L

# 에라토스체네스의 체 알고리즘 (소수 찾을 때 중요)
for i in range(2, int(L**0.5)+1):
    if p[i] == 1 :
        for j in range(i+i, L, i):
            p[j] = 0
prime = [i for i in range(2,L) if p[i] == 1]

# L을 넘는지 안넘는지만 확인해주면 됨
good, bad = 1,0   # 1 == True, 0 == False
for n in prime:
    if K%n == 0:
        good, bad = 0, n
        break
print("GOOD" if good else f"BAD {bad}")