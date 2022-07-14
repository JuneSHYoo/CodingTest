import sys

for i in range(3):
    N = int(sys.stdin.readline())
    list = [int(sys.stdin.readline()) for i in range(N)]
    
    if sum(list) == 0 :
        print("0")
    elif sum(list) > 0 :
        print("+")
    else:
        print("-")