# https://www.spoj.com/problems/ADDREV/

def reverse_no(no):
    new_no = 0
    for i in range(len(no)):
        new_no += int(no[i])*(10**i)
    return new_no

tc = int(input())

for _ in range(tc):
    no1, no2 = input().split(' ')
    ans = reverse_no(str(reverse_no(no1)+reverse_no(no2)))
    print(ans)
