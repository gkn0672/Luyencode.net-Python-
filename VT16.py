test = []
result = []
check = False
for i in input().split():
    test.append(int(i))

for i in test:
    if (i == 0):
        break
    if (i < 0):
        check = True
        result.append(i)
        

if(check == False):
    print("NOT FOUND")
else:
    print(*result, sep=" ")