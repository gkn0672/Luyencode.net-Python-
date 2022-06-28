a = int(input())
test = []
process = []
for i in input().split():
    test.append(int(i))

test = sorted(test)
res1 = test[a - 1] * test[a - 2] * test[a - 3]
res2 = test[0] * test[1] * test[a - 1]
if (res1 > res2):
    print(res1)
else:
    print(res2)