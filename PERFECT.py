n = int(input())
candidate = []
for i in input().split():
    candidate.append(int(i))

candidate.sort()
result = 10 ** 9
for i in range(2, n, 1):
    result = min(result, candidate[i] - candidate[i-1])

print(result)