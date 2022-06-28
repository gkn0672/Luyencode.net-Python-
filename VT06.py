a = int(input())
test = []
count = 0
for i in input().split():
    if (int(i) % 2 != 0):
        test.append(int(i))

average = sum(test) / len(test)

print(format(average, ".4f"))