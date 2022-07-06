t = int(input())
test = []
for i in range(t):
    test.append(int(input()))

formula = []
formula.append(1)

for i in range(1, 10 ** 6):
    formula.append((i + 1 + formula[i - 1]) ** 0.5)

for i in test:
    print(format(formula[i - 1], ".5f"))
