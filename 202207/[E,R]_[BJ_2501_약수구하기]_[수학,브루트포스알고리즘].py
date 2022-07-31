# BJ 2501 약수 구하기 <수학,브루트포스 알고리즘>
# https://www.acmicpc.net/problem/2501
# 시간 : 80 ms
# 문제 리뷰 : E , R
# 회고 : 반복문 조건문 한줄로 약수구하기

n, k = map(int, input().split(' '))
f_li = []
for i in range(1,int(n**0.5)+1):
    if n%i == 0 :
        f_li.append(i)
        f_li.append(n//i)
f_li = list(set(f_li))
f_li.sort()
print( f_li[k-1] if len(f_li) >= k else 0)

'''
Best Answer
n,k=map(int,input().split());print(*[i for i in range(1,1+n)if n%i<1][k-1:k]or[0])
'''