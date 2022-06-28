a = int(input())
test = []


for i in input().split():
    test.append(int(i))


print(*sorted(test, reverse=True), sep = " ")