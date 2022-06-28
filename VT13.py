a = int(input())
test = []
attempt = []

for i in input().split():
    test.append(int(i))

pre = 0
attempt.append(test[0] + test[len(test) - 1])
for i in range(len(test) - 1):
    attempt.append(test[i] + pre)
    pre = test[i]
maximum = max(attempt)

st = 0
ed = 0
for i in range(1, len(test)):
    check = test[i] + test[i-1]
    if(check == maximum):
        if(test[i-1] > st):
            st = test[i-1]
            ed = test[i]

if (st == 0):
    print("{0} {1}".format(test[len(test) - 1], test[0]))
else:
    print("{0} {1}".format(st, ed))

