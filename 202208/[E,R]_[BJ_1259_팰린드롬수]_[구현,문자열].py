# BJ 1259 팰린드롬수 <구현,문자열>
# https://www.acmicpc.net/problem/1259
# 시간 : 72 ms
# 문제 리뷰 : E , R
# 회고 : 문자열 혹은 리스트에 [::-1] 하면 요소들을 거꾸로 나타낼 수 있음

while 1:
    a = input()
    if a == '0':
        break
    answer = 'no'
    
    if a == a[::-1]:
        answer = 'yes'
    print(answer)