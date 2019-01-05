# https://www.youtube.com/watch?v=TC6snf6KPdE
def can_cows_be_arranged(difference, array, num_cows):
    count = 1
    curr = 0
    for i in range(1,stalls):
        if array[i] - array[curr] >= difference:
            count+=1
            curr = i
             
            # all cows were arranged based on condition
            if count >= num_cows:
                return True
    return False    

tc = int(input())

for _ in range(tc):
    stalls, no_of_cows = map(int, input().split())
    cows = []
    
    for i in range(stalls):
        cows.append(int(input()))

    cows.sort()
    low = 0
    high = cows[-1]

    while low < high:
        mid = low + (high-low+1)//2

        cows_arrange = can_cows_be_arranged(difference=mid, array=cows, num_cows = no_of_cows)

        # if current spec can arrange cows check for further in array
        # else no need to check further check the previos of array
        if cows_arrange:
            low = mid
        else:
            high = mid-1
    print(low)