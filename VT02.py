a = int(input())
test = []
for i in input().split():
    test.append(int(i))
    
result = sorted(set(test))
if (len(result) > 1):
    print(result[-2])
else:
    print("NOT FOUND")