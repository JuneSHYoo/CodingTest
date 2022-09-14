# PG 2022 kakao tech internship  성격 유형 검사하기 <코딩테스트연습>
# https://school.programmers.co.kr/learn/courses/30/lessons/118666
# 시간 : 72 ms
# 문제 리뷰 : M, P
# 회고 :

def solution(survey, choices):
    t = [{'R': 0 ,'T': 0},
       {'C':0,'F':0},
       {'J': 0 ,'M': 0} ,
       {'A': 0,'N': 0}]
    
    no = 0
    
    
    for s in survey:
        if 'R' in s : idx = 0 ;
        if 'C' in s : idx = 1 ;
        if 'J' in s : idx = 2 ;
        if 'A' in s : idx = 3 ;

        if choices[no] < 4 :
            t[idx][s[0]] += (4- choices[no])
        elif choices[no] > 4:
            t[idx][s[1]] += (choices[no] - 4)

        no += 1

    
    answer = ''
    for i in t:
        if i[list(i.keys())[0]] >= i[list(i.keys())[1]]:
            answer += list(i.keys())[0]
        else:
            answer += list(i.keys())[1]
        
    return answer