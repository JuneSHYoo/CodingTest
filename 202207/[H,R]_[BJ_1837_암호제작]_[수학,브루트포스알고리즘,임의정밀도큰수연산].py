# BJ 1837 암호제작 <수학, 브루트포스 알고리즘, 임의 정밀도 / 큰 수 연산>
# https://www.acmicpc.net/problem/1837
# 시간 : 352ms
# 문제 리뷰 : H , R
# 회고 :
'''
브루트포스 알고리즘 : 가능한 모든 경우의 수를 모두 탐색하는 알고리즘
소수를 구하는 에라토스체네스의 체를 사용하여 풀었다. 
'''

P, K = map(int, input().split())
li = [1]*K
for i in range(2, int(K**0.5)+1):
    if li[i] == 1:
        for j in range(i+i, K, i):
            li[j] = 0
prime = [i for i in range(2, K) if li[i] == 1]

good, bad = 1, 0
for n in prime:
    if P%n == 0:
        good, bad = 0, n
        break
print("GOOD" if good else f"BAD {bad}")