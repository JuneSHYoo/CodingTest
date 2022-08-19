# BJ 1524 세준세비 <구현,시뮬레이션>
# https://www.acmicpc.net/problem/1524
# 시간 : 180 ms
# 문제 리뷰 : M , R
# 회고 : sys.stdin.readline() 로 입력받을때 rstrip() 하고 안하고 차이가 있다.

import sys 
t = int(sys.stdin.readline())

for i in range(t):
    n,m = map(int, sys.stdin.readline().split())
    s = map(int, sys.stdin.readline().split())
    b = map(int, sys.stdin.readline().split())
    
    if max(s) >= max(b):
        print("S")
    else:
        print("B")
        
    
'''
한줄코딩
for _ in range(int(input())):input();input();print(['S','B'][max(map(int,input().split()))<max(map(int,input().split()))])
'''