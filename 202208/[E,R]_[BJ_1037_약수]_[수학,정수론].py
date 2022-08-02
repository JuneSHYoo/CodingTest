# BJ 1037 약수 <수학,정수론>
# https://www.acmicpc.net/problem/1037
# 시간 : 72 ms
# 문제 리뷰 : E , R
# 회고 : * 연산자로 입력 받을때 리스트 형태로 바로 저장할 수 있다. 

n = int(input())
fac = list(map(int, input().split()))
fac.sort()
print(fac[len(fac)-1]*fac[0])

'''
input()
*a,=map(int,input().split())
print(max(a)*min(a))
'''
