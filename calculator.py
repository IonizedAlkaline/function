def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


choice = input("enter thhe operation")
num1 = int(input("enter the number"))
num2 = int(input("enter the number"))

if choice == "+":
    print(f"the sum of{num1} and {num2} is {add(num1,num2)}")

elif choice == "-":
    print(f"the difference of{num1} and {num2} is {sub(num1,num2)}")

elif choice == "*":
    print(f"the product of,{num1}, and {num2} is {mul(num1,num2)}")

else:
    print(f"the quotient of,{num1}, and ,{num2}, is ,{div(num1,num2),}")
