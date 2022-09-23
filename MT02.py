row, col = [int(i) for i in input().split()]
total = 0
oned = [int(i) for i in input().split()]
for i in range(row):
    for j in range(col):
        num = oned.pop(0)
        if(i % 2 != 0):
            total += num
        
print(total)

