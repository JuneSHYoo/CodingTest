# BJ 1816 암호 키 <수학,브루트포스 알고리즘, 정수론>
# https://www.acmicpc.net/problem/1816
# 시간 : 3628 ms
# 문제 리뷰 : H , R
# 회고 :

n = int(input())

for _ in range(n):
    k = int(input())
    
    nums = [0]*(10**6+1)
    for i in range(2, 10**6+1):
        if nums[i] == 0:
            for j in range(i, 10**6+1, i):
                nums[j] = 1
            
            if k % i == 0 :
                print('NO')
                break
    else:
        print('YES')
        
        
'''
풀이 
에라토스테레스의 체를 이용하여 풀이
체 원래는 2~k까지 확인해야하지만, 이 문제는 100만까지의 소수로 나눠지는지 확인하면 됨
100만 이하의 소수로 나눠지면 'NO' 아니면 'YES'
'''