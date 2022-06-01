"""Calculator"""

what = input("What action do you want to perform? (+,-,*,/):")

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if what == "+":
    c: float = a + b
    print("Reply: " + str(c))
elif what == "-":
    c = a - b
    print("Reply: " + str(c))
elif what == "*":
    c = a * b
    print("Reply: " + str(c))
elif what == "/":
    c = a / b
    print("Reply: " + str(c))
else:
    print("Incorrect operation selected!")

