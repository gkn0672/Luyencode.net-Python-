test = []
result = []

for i in input().split():
    test.append(int(i))

a = test.pop()

def check(key):
    try:
        index = test.index(key)
        result.append(index + 1)
        test[index] = key - 1
    except:
        return 0

while (check(a) != 0):
    check(a)

if (len(result) < 1):
    print(-1)
else:
    print(*result, sep=" ")