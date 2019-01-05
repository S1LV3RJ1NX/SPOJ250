tc = int(input())

for _ in range(tc):
    sum=0
    n = input()
    men = sorted([int(x) for x in input().split(' ')])
    women = sorted([int(x) for x in input().split(' ')])
  
    for x in range(int(n)):
        sum+= (men[x]*women[x])

    print(sum)
