# http://www.algorithmist.com/index.php/SPOJ_STPAR

n = int(input())

while n:
    side_street = []
    # cars = []
    curr_car = 1

    flag = True
    cars = [int(x) for x in input().split()]
    # print(cars)
    for i in range(n): 

        while len(side_street) != 0 and side_street[-1] == curr_car:
            curr_car+=1
            side_street.pop()
        
        if cars[i] == curr_car:
            curr_car+=1

        elif len(side_street) != 0 and side_street[-1] < cars[i]:
            flag = False
            break 
        else:
            side_street.append(cars[i])

    if flag:
        print("yes")
    else:
        print("no")
    n = int(input())