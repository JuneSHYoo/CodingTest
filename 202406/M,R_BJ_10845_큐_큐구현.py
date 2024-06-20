# BJ 10828 큐 <큐,구현>
# https://www.acmicpc.net/problem/10845
# 시간 : 44 ms
# 문제 리뷰 : M, R
# 회고 : 스택,큐 응용문제도 풀어봐야겠다..

import sys
n = int(sys.stdin.readline())

queue = []
for i in range(n):
  inplst = sys.stdin.readline().split()

  if inplst[0] == 'push' :
    queue.append(inplst[1])

  if inplst[0] == 'pop' :
    if (len(queue) > 0 ) :
      print(queue.pop(0))
    else :
      print(-1)

  if inplst[0] == 'size' :
    print(len(queue))

  if inplst[0] == 'empty' :
    if len(queue) == 0 : print(1)
    else : print(0)
  
  if inplst[0] == 'front' :
     if (len(queue) > 0 ) :
      print(queue[0])
     else :
      print(-1)

  if inplst[0] == 'back' :
     if (len(queue) > 0 ) :
      print(queue[-1])
     else :
      print(-1)