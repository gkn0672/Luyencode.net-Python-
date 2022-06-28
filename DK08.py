a, operator, b = [str(ele) for ele in input().split()]
num1 = float(a)
num2 = float(b)

try:
    if(operator == "+"):
        print(format(num1 + num2, '.2f'))
    elif(operator == "-"):
        print(format(num1 - num2, '.2f'))
    elif(operator == "*"):
        print(format(num1 * num2, '.2f'))
    else:
        print(format(num1 / num2, '.2f'))
except:
    print("Math Error")