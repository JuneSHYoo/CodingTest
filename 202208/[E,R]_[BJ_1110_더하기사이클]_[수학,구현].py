# BJ 1110 더하기 사이클 <수학,구현>
# https://www.acmicpc.net/problem/1110
# 시간 : 68 ms
# 문제 리뷰 : E , R
# 회고 : 코끼리 연산자(:=)와 while 이용해 간단하게 풀 수 있다. 

a = input().zfill(2)
cnt = 0 
a_org = a
while 1:
    a = a[1]+str(int(a[0])+int(a[1])).zfill(2)[1]
    cnt += 1
    if a_org == a:
        break
print(cnt)

'''
Best Answer
a=n=int(input());c=1
while(a:=a%10*10+a*11//10%10)-n:c+=1
print(c)
'''