t = int(input())
test = []
for i in range(t):
    test.append(int(input()))
formula = []
formula.append(0)
for i in range(1, 10 ** 6):
    formula.append(formula[i - 1] + (1/i))
for i in test:    
    print(format(formula[i], ".5f"))
