a = int(input())
test = []
result = []

for i in input().split():
    test.append(int(i))

def check(n):
    if(n < 2):
        return False
    elif(n == 3):
        return True
    else:
        for i in range(2, int(n ** 0.5 + 1)):
            if (n % i == 0):
                return False
        return True

for i in range(len(test)):
    if((check(test[i]) == True) and (test[i] not in result)):
        result.append(test[i])
result = sorted(result)  
print(*result, sep = " ")