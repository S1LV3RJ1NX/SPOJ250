# https://www.spoj.com/problems/FCTRL/
# solun:- https://algorithm3.wordpress.com/2012/03/29/11-factorial/

tc = int(input())

for _ in range(tc):
    n = int(input())
    ans = 0

    while(n>=5):
        ans+= n//5
        n//=5

    print(ans)
