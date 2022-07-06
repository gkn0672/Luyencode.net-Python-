t = int(input())
test = []

for i in range(t):
    test.append(int(input()))

formula = []
formula.append(0.0)
formula.append(1.0)

for i in range(2, 10 ** 6):
    formula.append(formula[i - 1] + (1.0 /(2.0 * i - 1)))

for i in test:
    print(format(formula[i], ".5f"))