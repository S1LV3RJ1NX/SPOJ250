c = float(input())

while c:
    card_len = 0.0
    ans = 0

    while card_len < c:
        ans+=1
        card_len+= 1.00/(1.00+ans)

    print(ans,"card(s)")
    c = float(input())