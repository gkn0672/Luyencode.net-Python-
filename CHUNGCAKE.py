n, v = [int(i) for i in input().split()]
cake = []
for i in input().split():
    cake.append(int(i))

minval = min(cake)
if(minval > v):
    print(0)
else:
    dp = []
    for i in range(0, v+1, 1):
        dp.append(0)


    dp[0] = 1
    for i in range(n):
        for j in range(v, cake[i] - 1, -1):
            if(dp[j-cake[i]] == 1):
                dp[j] = 1
    
    for i in range(v, minval -1, -1):
        if(dp[i] == 1):
            print(i)
            break



