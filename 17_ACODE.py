# ref:- https://stackoverflow.com/questions/9050903/spoj-alpha-code
# ref:- https://www.youtube.com/watch?v=IpveX_c4vfQ
# ref:- https://www.youtube.com/watch?v=Y3y64ge9ioU

while True:
    string = input()
    if string == '0':
        break 
    dp = [0]*(len(string)+1)
    dp[0] = dp[1] = 1 # fst char only one way

    for i in range(2, len(string)+1):
        prev_digit = int(string[i-2])
        curr_digit = int(string[i-1])

        # since valid combinations are between 1 to 26
        if (prev_digit>=3 or prev_digit==0):
            dp[i] = dp[i-1]
        else:
            # prev_digit is 1 or 2
            if(curr_digit==0):
                dp[i] = dp[i-2]
            else:
                if(prev_digit == 2 and curr_digit>6):
                    dp[i] = dp[i-1]
                else:
                    dp[i] = dp[i-1] + dp[i-2]
    print(dp[len(string)])