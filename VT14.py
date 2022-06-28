a = int(input())
test = []

for i in input().split():
    test.append(int(i))

test = sorted(test)
result1 = test[len(test) - 1] * test[len(test) - 2]
result2 = test[0] * test[1]
if(result1 > result2):
    print(result1)
else:
    print(result2)

