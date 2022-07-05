a, b, c, d = [int(i) for i in input().split()]
def swap(a, b):
    temp = a
    a = b
    b = temp
if(a > b):
    swap(a, b)
if(c > d):
    swap(c, d)
if((b < c) or (a > d)):
    print("NO")
else:
    print("YES")