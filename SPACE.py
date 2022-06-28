a = int(input())
test = []
for i in range(a):
    s = input()
    test.append(s)

for i in test:
    attempt = list(i)
    count = 0
    for j in range(0, len(attempt) - 1):
        if((attempt[j] == " ") and (attempt[j + 1] != " ")):
            count += 1
    if(attempt[len(attempt) - 1] == " "):
        count += 1
    print(count)