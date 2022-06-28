a = int(input())
test = []
for i in input().split():
    test.append(int(i))

maximum = max(test)
index = test.index(maximum)
test[index] = -1
while(max(test) == maximum):
    new_idx = test.index(max(test))
    if new_idx > index:
        index = new_idx
        test[index] = -1

print(index)