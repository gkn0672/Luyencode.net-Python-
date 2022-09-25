s = input()
s = s.lower()
count_alpha = []
count_digit = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
number = "0123456789"

for i in range(26):
    count_alpha.append(0)

for i in range(10):
    count_digit.append(0)

def convert_c(char):
    return ord(char) - 97

def convert_d(char):
    return ord(char) - 48

for i in s:
    if(i.isalpha()):
        count_alpha[convert_c(i)] += 1
    if(i.isdigit()):
        count_digit[convert_d(i)] += 1

for i in range(10):
    if(count_digit[i] != 0):
        print("{0} {1}".format(number[i], count_digit[i]))

for i in range(26):
    if(count_alpha[i] != 0):
        print("{0} {1}".format(alphabet[i], count_alpha[i]))


