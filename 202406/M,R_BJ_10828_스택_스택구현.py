# BJ 10828 스택 <스택,구현>
# https://www.acmicpc.net/problem/10828
# 시간 : 40 ms
# 문제 리뷰 : M, R
# 회고 : java만 쓰다가 오랜만에 python 하니깐 너무 헷갈린다..! 시간 줄이는 명령어들도 기억해둬야지!

import sys
n = int(sys.stdin.readline())

stack = []
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push' :
        stack.append(int(command[1]))
    
    elif command[0] == 'pop' :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack.pop())
    
    elif command[0] == 'top' :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[-1])
    
    elif command[0] == 'size' :
        print(len(stack))
    
    elif command[0] == 'empty' :
        if len(stack) == 0 : print(1)
        else : print(0)