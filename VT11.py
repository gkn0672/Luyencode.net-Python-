a = int(input())
test = []
result = []

for i in input().split():
    test.append(int(i))

st = test.pop(0)
ed = test.pop(-1)
test = sorted(test)
result.append(st)

for i in range(len(test)):
    result.append(test[i])
result.append(ed)

print(*result, sep = " ")


    

     




        
