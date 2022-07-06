t = int(input())
test = []
for i in range(t):
    test.append(int(input()))

formula = []
formula.append(1)

def compute(n):
    ans = n ** 0.5
    for i in range(n - 1, 0, -1):
        ans = (i + ans) ** 0.5
    return ans

for i in test:
    print(format(compute(i), ".5f"))

