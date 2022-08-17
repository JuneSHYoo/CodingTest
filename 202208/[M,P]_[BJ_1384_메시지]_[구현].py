# BJ 1384 메시지 <구현>
# https://www.acmicpc.net/problem/1384
# 시간 : 72 ms
# 문제 리뷰 : M , P
# 회고 :

no = 1
while 1:
    n = int(input())
    
    if n == 0 :
        break
        
    grp = {}
    name = []
    for i in range(n):
        *a, = input().split()
        grp[a[0]] = a[1:]
        name.append(a[0])
    
    print(f"Group {no}")
    
    nasty = 'no'
    for key in grp:
        if "N" in grp[key]:
            for i in range(grp[key].count("N")):
                nasty = 'yes'
                nm = name[name.index(key)-(grp[key].index("N")+1)]
                print(f"{nm} was nasty about {key}")
                grp[key][grp[key].index("N")] = "P"

    if nasty == "no":
                  print("Nobody was nasty")    
    print("")
    no += 1