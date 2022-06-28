a, key = [int(i) for i in input().split()]
test = []
for i in input().split():
    test.append(int(i))
try:
    target = test.index(key)
    print("YES")
except:
    print("NO")