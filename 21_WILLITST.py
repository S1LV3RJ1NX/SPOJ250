n = int(input())

while n>1:

    if n%3==0:
        print("NIE")
        exit(0)
    if n%2 == 0:
        n = n//2
    else:
        n = 3*n+3
print("TAK")