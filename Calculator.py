a = int(input("Enter a number1: "))
b = int(input("Enter a number2: "))
oper = input("Enter the type of operation you want to use( +,-, %,*,/)")

result = 0
if oper == "+":
    result = a+b
elif oper == "-":
    result = a - b
elif oper == "*":
    result = a*b
elif oper == "/":
    result = a//b
elif oper == "%":
    result = a%b
else:
    print("invalid operator")
print("Your answer is:", result)