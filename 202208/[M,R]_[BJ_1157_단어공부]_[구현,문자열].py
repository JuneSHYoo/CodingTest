# BJ 1157 단어공부 <구현,문자열>
# https://www.acmicpc.net/problem/1157
# 시간 : 2028 ms
# 문제 리뷰 : M , R
# 회고 : 알파벳 개수 오름차순으로 알파벳을 정렬 (?가 가장 앞에 나오도록) 개수 비교해서 true 이면 가장 마지막 false이면 ? 출력

'''
Best Answer
s=input().upper();c=s.count;*_,a,b=v=sorted({*s,'?'},key=c);print(v[-(c(a)<c(b))])
'''
a = input().lower()
a_org = a
a_unq = list(set(a))
mx  = 0
mx_c = ''
for i in a_unq:
    cnt=0 
    for j in a_org:
        if i == j :
            cnt += 1
    if mx < cnt :
        mx = cnt
        mx_c = i
    elif mx == cnt :
        mx_c ='?'
print(mx_c.upper())