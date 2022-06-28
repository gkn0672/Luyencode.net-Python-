import re
a = int(input())
my_str = input()
pattern = my_str[0]
key = my_str[-1]
n = 0
answer = False
remain = 0
while(True):
    n += 1
    pattern += my_str[n]
    attempt = re.findall(pattern, my_str)
    compute = (a - 1) - (len(attempt) * len(pattern))
    if(compute <= len(pattern)):
        remain = compute
        break
    
if( remain == 0):
    print(pattern[0])
else:
    print(pattern[1])



        



