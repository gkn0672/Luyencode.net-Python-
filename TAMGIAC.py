a, b, c = [int(i) for i in input().split()]
if((a + b > c) and (a + c > b) and (b + c > a)):
    p = a + b + c
    print(p, end = " ")
    hp = p / 2
    s = (hp * (hp - a) * (hp - b) * (hp - c)) ** 0.5
    print(format(s, ".2f"))
else:
    print("NO")