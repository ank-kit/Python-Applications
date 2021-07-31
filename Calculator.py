#1. Calculator

num1 = int(input("Please enter first number : "))

num2 = int(input("Please enter second number : "))

op = input("Please select your operator- +,-,*,/ ")

if op == "+" :

    print(num1 + num2)

elif op == "-" :

    print(num1 - num2)

elif op == "*" :

    print(num1 * num2)

else:

    print(num1 / num2)