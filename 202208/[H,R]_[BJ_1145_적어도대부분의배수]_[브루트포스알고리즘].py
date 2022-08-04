# BJ 1145 적어도 대부분의 배수 <브루트포스알고리즘>
# https://www.acmicpc.net/problem/1145
# 시간 : 712 ms
# 문제 리뷰 : H , R
# 회고 : 가장 작은 수를 증가시키면서 5개의 숫자들로 나누었을때 나머지가 0인 숫자의 개수가 3개 이상이라면 그 숫자 출력해주고 while문 빠져나오기

*a, = map(int, input().split())
n = min(a)

while 1:
    cnt = 0 
    for i in range(5):
        if n % a[i] == 0 :
            cnt += 1
    if cnt > 2: 
        print(n)
        break 
    n += 1