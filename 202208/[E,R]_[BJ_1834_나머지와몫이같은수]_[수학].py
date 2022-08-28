# BJ 1834 나머지와 몫이 같은 수 <수학>
# https://www.acmicpc.net/problem/1834
# 시간 : 272 ms
# 문제 리뷰 : E , R
# 회고 :

n = int(input())
num = 0
for i in range(n + 1, n ** 2, n + 1):
    num += i
print(num)


'''
풀이
나머지와 몫이 같은 수는 n+1부터 n의 제곱까지 존재하게 된다. 
그리고 n+1의 배수
'''