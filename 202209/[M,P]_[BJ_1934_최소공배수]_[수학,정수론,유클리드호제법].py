# BJ 1934 최소공배수 <수학,정수론,유클리드호제법>
# https://www.acmicpc.net/problem/1934
# 시간 : 194 ms
# 문제 리뷰 : M , P
# 회고 :


num = int(input())
for i in range(num):
    a,b = map(int, input().split())
    A,B = a,b
    while a!= 0 :
        b = b%a
        a,b = b,a
        
    gcd = b
    lcm = A*B//b
    print(lcm)
    
'''
둘중에 작은수와 큰 수에서 작은 수를 나눈 나머지와의 최대공약수가 같다.
작은수가 0 이 되면 그때 큰 수가 최대공약수가 된다. 

최소공배수는 주어진 수 하나는 그대로 곱하고 하나는 최대공약수로 나눠서 곱해준다.
'''