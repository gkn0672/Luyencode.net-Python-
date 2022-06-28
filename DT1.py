import math
pi = math.pi
a = int(input())

def process(n):
    tamgiac = (n ** 2) / 2
    cungtron = (0.5 * (n ** 2) * (pi /2)) - tamgiac
    result = 2 * tamgiac + 2 * cungtron
    return result
print(format(process(a), ".3f"))

