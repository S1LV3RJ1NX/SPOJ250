
'''As rectanglesof i*j size with N squares must have i*j=N
therefore i and j are factors of N.
for e.g rectangle of 2*3 must have 6 unit squares.

Therefore no. of rectangles using all N squares is the number of pairs of factors of N which when multiplied result to N.

But pairs are found in couple as for N=6 2*3 and 3*4 both reuslt to N but we have to take only one .
Hence we will only find the no. of factors of N upto squareroot of N.
'''
n = int(input())
sum = 0
for i in range(1,n+1):
    x = int(i**0.5)
    for j in range(1,x+1):
        if i%j ==0:
            sum+=1
print(sum)
