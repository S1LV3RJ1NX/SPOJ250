# https://www.spoj.com/problems/NSTEPS/
tc = int(input())

for _ in range(tc):
    x,y = map(int, input().split())

    if (x==y):
        if (x%2==0 and y%2==0):
            print(x+y)
        else:
            print(x+y-1)
    elif (y==x-2):
        if (x%2==0 and y%2==0):
            print(x+y)
        else:
            print(x+y-1)

    else:
        print("No Number")
