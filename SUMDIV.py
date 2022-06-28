test = []
a = int(input())
for i in range(a):
    test.append(int(input()))

def sum(n):
    total = 0
    for i in range(1, int(n ** 0.5) + 1):
        if (n % i == 0):
            j = int(n / i)
            if(i == j):
                total += i
            else:
                total += i + j
    return total

for i in test:
    print(sum(i))
    

  