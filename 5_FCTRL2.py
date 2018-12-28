# https://www.spoj.com/problems/FCTRL2/
tc = int(input())
fact = [0]*101
fact[0] =  1

for _ in range(tc):
    n = int(input())
    if fact[n] != 0:
        print(fact[n])
    else:
        for i in range(1,n+1):
            fact[i] = i*fact[i-1]
        print(fact[n])
