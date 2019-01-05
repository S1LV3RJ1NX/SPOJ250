letters = 'abcdefghijklmnopqrstuvwxyz'
operators = ['+','-','*','/','^']
stack = []
tc = int(input())

for _ in range(tc):
    str_ = input()
    ans = ''
    for x in range(len(str_)):
        if str_[x] == '(':
            continue
        elif  str_[x] in letters :
            ans+= str_[x]
        elif str_[x] in operators:
            stack.append(str_[x])
        elif str_[x] == ')':
            ans+= stack.pop()
    print(ans)
