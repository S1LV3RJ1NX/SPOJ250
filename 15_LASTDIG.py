tc = int(input())

# fast modular exp for (x^y)%p
def power(x,y,p=10):
    res = 1

    # update x if x>= p
    x = x%p

    while y>0:
        # if y is odd multiply with the result
        if ((y&1)==1):
            res = (res*x)%p

        # y must be even now
        y = y>>1
        x = (x*x)%p
    
    return res
        
        
for _ in  range(tc):
    a,b = map(int, input().split(' '))
    print(power(a,b))