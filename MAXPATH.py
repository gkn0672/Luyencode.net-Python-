a, b = [int(i) for i in input().split()]
test = [] 
pos = 0

#Read array
for i in range(a):
    test.append([int(i) for i in input().split()])

#create answer array
ans = []
for i in range(a + 2):
    ans.append([0 for j in range(b + 2)])
    
#process
for i in range(1, b + 1):
    for j in range(1, a + 1):
        compute = max(ans[j - 1][i - 1], ans[j][i - 1], ans[j + 1][i - 1]) + test[j - 1][i - 1]
        ans[j][i] = compute
            
            

#print result
result = []
for i in range(1, a + 1):
    result.append(ans[i][b])
total = max(result)
print(total)


    
    
    
    
    
