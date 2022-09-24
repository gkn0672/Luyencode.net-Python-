row, col, target = [int(i) for i in input().split()]
arr = []
arrcol = []
oned = [int(i) for i in input().split()]
for i in range(row):
    temp = []
    for j in range(col):
        temp.append(oned.pop(0))
    arrcol.append(temp[target - 1])
    arr.append(list(temp))   


arrcol.sort()

for i in range(row):
    for j in range(col):
        if(j == target - 1):
            print(arrcol.pop(0), end = " ")
        else:
            print(arr[i][j], end = " ")
    print()
