test = []
a = int(input())
for i in range(a):
    test.append(int(input()))

for i in test:
    print(format(2 * (1 - (1/(i + 1))), ".8f"))
    

    

  