n, c = [int(i) for i in input().split()]
ngo = []
for i in input().split():
    ngo.append(int(i))  

def knapsack(n, c):
    if ((n == 0) or (c == 0)):
        result = 0
    elif (ngo[n - 1] > c):
        result = knapsack(n - 1, c)
    else:
        candidate1 = knapsack(n - 1, c)
        candidate2 = ngo[n - 1] + knapsack(n - 1, c - ngo[n - 1])
        result = max(candidate1, candidate2)
    return result

print(knapsack(n, c))

    
            

        

        
    
       
    