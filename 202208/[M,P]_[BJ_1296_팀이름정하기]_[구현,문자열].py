# BJ 1296 팀 이름 정하기 <구현, 문자열>
# https://www.acmicpc.net/problem/1296
# 시간 : 92 ms
# 문제 리뷰 : M , P
# 회고 :

import sys

def solution() :
    y = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    std = list('LOVE')
    
    if n == 1 :
        print(sys.stdin.readline().rstrip())
    else :
        res = []
        for _ in range(n) :
            s = sys.stdin.readline().rstrip()
                
            calc = 1
            for i in range(len(std)) :
                for j in range(i+1, len(std)) :
                    calc *= (y.count(std[i]) + s.count(std[i])) + (y.count(std[j]) + s.count(std[j]))
            
            res.append((calc % 100, s))
        
        res.sort(key = lambda x : (-x[0], x[1]))

        print(res[0][1])
                                 
solution()