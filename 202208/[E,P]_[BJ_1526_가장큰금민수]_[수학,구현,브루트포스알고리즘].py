# BJ 1526 가장 큰 금민수 <수학, 구현, 브루트포스 알고리즘>
# https://www.acmicpc.net/problem/1526
# 시간 : 344 ms
# 문제 리뷰 : E , P
# 회고 : asterisk(*) 를 이용해 positional 가변인자를 세트로 패킹할 수 있다. 참고로 keyword 가변인자일 경우 {**변수명}

n = input()

while True:
    if len(n) == n.count('4') + n.count('7'):
        print(n)
        break
    n = str(int(n) -1)
    

'''
짧은 코딩
N=int(input())
while{*str(N)}-{*'47'}:N-=1
print(N)
'''