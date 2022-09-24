row, col, target = [int(i) for i in input().split()]
arr = []
oned = [int(i) for i in input().split()]
for i in range(row):
    temp = []
    for j in range(col):
        temp.append(oned.pop(0))
    arr.append(list(temp))   

arr[target - 1].sort()

for i in range(row):
    for j in range(col):
        print(arr[i][j], end = " ")
    print()
