n, k = [int(i) for i in input().split()]
test = []

for i in input().split():
    test.append(int(i))
    
score = []
score.append(0)

for i in range(1, n + 1):
    init_max = score[max(0, i - k)]
    for j in range(max(0, i-k), i):
        init_max = max(init_max, score[j])
    score.append(init_max + test[i - 1])
    final_max = max(init_max, score[i])


print(final_max)