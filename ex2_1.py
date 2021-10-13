import math

print("Welcome to the calculator...")

while(True):
    print("\nChoose an option :")
    print("1- Sum")
    print("2- Sub")
    print("3- Mul")
    print("4- Div")
    print("5- Sin")
    print("6- Cos")
    print("7- Tan")
    print("8- Cot")
    print("9- Log")
    print("0- Exit")

    select = int(input())

    if select == 1:
        print("Enter two numbers :")
        a = float(input())
        b = float(input())
        c = a + b
        print("Sum is : " , c)

    elif select == 2:
        print("Enter two numbers :")
        a = float(input())
        b = float(input())
        c = a - b
        print("Sub is : " , c)

    elif select == 3:
        print("Enter two numbers :")
        a = float(input())
        b = float(input())
        c = a * b
        print("Mul is : " , c)
        

    elif select == 4:
        print("Enter two numbers :")
        a = float(input())
        b = float(input())

        if b != 0:
            c = a / b
            print("Div is : " , c)
        else:
            print('Cannot divide by 0')

    elif select == 5:
        print("Enter the degree :")
        a = float(input())
        c = math.sin(math.radians(a))
        print("Sin is : " , c)

    elif select == 6:
        print("Enter the degree :")
        a = float(input())
        c = math.cos(math.radians(a))
        print("Cos is : " , c)   

    elif select == 7:
        print("Enter the degree :")
        a = float(input())
        c = math.tan(math.radians(a))
        print("Tan is : " , c) 

    elif select == 8:
        print("Enter the degree :")
        a = float(input())
        c = math.atan(math.radians(a))
        print("Cot is : " , c)

    elif select == 9:
        print("Enter the number :")
        a = float(input())
        c = math.log10(a)
        print("Log is : " , c)

    elif select == 0:
        break
    
    else:
       print('not found. try again')

