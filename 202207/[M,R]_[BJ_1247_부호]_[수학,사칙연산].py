# BJ 1247 부호 <수학,사칙연산,임의 정밀도 / 큰 수 연산>
# https://www.acmicpc.net/problem/1247
# 시간 : 248ms
# 문제 리뷰 : M , R
# 회고 : 빠르게 입력받는 sys.stdin.readline() , 연속적으로 숫자를 입력받을 때 반복문+리스트로 한 줄로 입력 가능

import sys

for i in range(3):
    N = int(sys.stdin.readline())
    list = [int(sys.stdin.readline()) for i in range(N)]
    
    if sum(list) == 0 :
        print("0")
    elif sum(list) > 0 :
        print("+")
    else:
        print("-")