test = []
result = []
a = int(input())
for i in input().split():
    test.append(int(i))
    
for i in range(len(test)):
    result.append(1)

for i in range(0, len(test) - 1):
    for j in range(i + 1, len(test)):
        if ((test[j] > test[i]) and (result[j] < result[i] + 1) ):
            result[j]  = result[i] + 1
      
print(max(result))

