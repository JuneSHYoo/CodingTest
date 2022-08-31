# BJ 1924 2007년 <수학,구현>
# https://www.acmicpc.net/problem/1924
# 시간 : 68 ms
# 문제 리뷰 : E , P
# 회고 :

m,d = map(int, input().split())
mon = [0,31,28, 31,30,31,30,31,31,30,31,30,31]
day = ['SUN','MON','TUE','WED','THU','FRI','SAT']

days = 0
for i in range(m):
    days += mon[i]
print(day[(days+d) % 7])