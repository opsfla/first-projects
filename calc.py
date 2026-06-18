import math

while True:
    Num1 = int(input("Number 1: "))
    operation = input(" ")
    Num2 = int(input("Number 2: "))

    if operation == '+':
     Sum = Num1 + Num2 
    elif operation == '-':
     Sum = Num1-Num2
    elif operation == '*':
     Sum = Num1*Num2
    elif operation == '/':
     Sum = Num1/Num2
    print(f"{Num1}{operation}{Num2} = {round(Sum,1)}")

    Clear = input("Try another?:y/n ") 
    if Clear != 'y':
     break