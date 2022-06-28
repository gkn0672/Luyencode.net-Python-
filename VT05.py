a, key = [int(i) for i in input().split()]
test = []
count = 0
for i in input().split():
    test.append(int(i))

def check(key):
    try:
        test.index(key)
        test[test.index(key)] = key - 1
    except:
        return 0

while(check(key) != 0):
    count += 1
print(count)