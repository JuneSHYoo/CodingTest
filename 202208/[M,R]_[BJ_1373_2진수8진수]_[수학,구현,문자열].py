# BJ 1373 2진수 8진수 <수학, 구현, 문자열>
# https://www.acmicpc.net/problem/1373
# 시간 : 76 ms
# 문제 리뷰 : M , R
# 회고 : 2진수, 8진수, 16진수 변환 = bin(), oct(), hex() // 문자열 숫자로 변환 = int( , base)

print(oct(int(input(),2))[2:])