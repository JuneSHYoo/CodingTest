# BJ 2010 플러그 <수학,사칙연산,구현>
# https://www.acmicpc.net/problem/2010
# 시간 : 236ms
# 문제 리뷰 : E, P
# 회고 : 

import sys
print( sum([ int(sys.stdin.readline())-1 for i in range( int(sys.stdin.readline()))]) + 1)