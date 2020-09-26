"""24.9.20 - 25.9.20
author-manas verma
design a calculator which will correctly solve all the problems except this following ones:-
1)45*3=555
2)56+9=77
3)56/6=4
Your program should take operator and two numbers as input and then return the result"""
# making a faulty calculator
operator = input("Enter operator:")
val1 = int(input("Enter first number = "))
val2 = int(input("Enter second number = "))

if operator == "+":
    if val1 == 56 and val2 == 9:
        print("sum is 77")
    else:
        print("Sum is:",val1 + val2)
if operator == "-":
    print("Substract is:",val1-val2)
if operator == "*":
    if val1 == 45 and val2 == 3:
        print("multiply is 555")
    else:
        print("Multiply is :",val1*val2)
if operator == "/":
    if val1 ==56 and val2 == 6:
        print("divide is 4")
    else:
        print("Divide is:",float(val1/val2))









