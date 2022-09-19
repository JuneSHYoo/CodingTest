# BJ 2204 도비의 난독증 테스트 <문자열, 정렬>
# https://www.acmicpc.net/problem/2204
# 시간 : 104 ms
# 문제 리뷰 : E, R
# 회고 : sort(key = str.lower) 로 문자열 비교 후 정렬 가능

while True:
    vocab = [] 
    n = int(input())
    if n == 0:
        quit() 
    for i in range(n):
        vocab.append(input())
        
    vocab.sort(key= str.lower)
    print(vocab[0])