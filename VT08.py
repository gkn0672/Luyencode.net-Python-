a = int(input())
test = []
result = []

for i in input().split():
    test.append(int(i))

def process(n):
    left = 0
    right = 0
    if (n - 1 < 0):
        left = 0
    else:
        left = test[n-1]
    if (n + 1 > len(test) - 1):
        right = 0
    else:
        right = test[n+1]
    return abs(left - right)
    
for i in range(len(test)):
    if (i % 2 != 0):
        test[i] = test[i] + process(i)

print(*test, sep = " ")
    

     




        
