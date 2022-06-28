test = []
a = int(input())
for i in range(a):
    test.append(input())

for i in test:
    attempt = []
    process = [char for char in i]
    for each in process:
        attempt.append(int(each))
    print(sum(attempt))

  