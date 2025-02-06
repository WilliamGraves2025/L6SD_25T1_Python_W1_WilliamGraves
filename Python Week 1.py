def Techtorium():
    print("\033[H\033[J", end="")
    print("Enter a day")
    answer = int(input())
    day = answer
    if day == 1:
        D1()
    elif day == 2:
        print("This day is currently incomplete, please try again later")
        #D2()
    elif day == 3:
        print("This day is not in this program")
    elif day == 4:
        print("This day is a public holiday")
    elif day == 5:
        print("This day is not in this program")
    else:
        print("Invalid day")

def D1():
        print("Enter a task")
        answer = int(input())
        task = answer
        if task == 1:
            Calculators()
        elif task == 2:
            Numbers()
        elif task == 3:
            Voting()
        elif task == 4:
            Equasion()
        elif task == 5:
            Calculator()
        else:
            print("Invalid task")

def Calculators():
    print("Enter a calculator")
    answer = int(input())
    calculator = answer
    if calculator == 1:
        Calculator1()
    elif calculator == 2:
        Calculator2()
    elif calculator == 3:
        Calculator3()
    elif calculator == 4:
        Calculator4()
    else:
        print("Invalid calculator")

def D2():
    print("Enter a task")
    answer = int(input())
    task = answer
    if task == 1:
        Name()
    elif task == 2:
        Numbers2()
    elif task == 3:
        Colours()
    elif task == 4:
        Lines()
    elif task == 5:
        Format()
    elif task == 6:
        Hello()
    elif task == 7:
        Swap()
    elif task == 8:
        Concentration()
    elif task == 9:
        Initialisation()
    elif task == 10:
        Calculator5()
    elif task == 11:
        Comparison()
    elif task == 12:
        Strings()
    elif task == 13:
        IfElse()
    elif task == 14:
        NestedIf()
    elif task == 15:
        Repeat()
    else:
        print("Invalid task")


def Calculator1():
    print("Enter a number")
    answer = int(input())
    number1 = answer
    print(" ")
    print("Enter another number")
    answer = int(input())
    number2 = answer
    number3 = number1 + number2
    print(" ")
    print("The answer is")
    print(number3)

def Calculator2():
    print("Enter a number")
    answer = int(input())
    number1 = answer
    print(" ")
    print("Enter another number")
    answer = int(input())
    number2 = answer
    number3 = number1 - number2
    print(" ")
    print("The answer is")
    print(number3)

def Calculator3():
    print("Enter a number")
    answer = int(input())
    number1 = answer
    print(" ")
    print("Enter another number")
    answer = int(input())
    number2 = answer
    number3 = number1 * number2
    print(" ")
    print("The answer is")
    print(number3)

def Calculator4():
    print("Enter a number")
    answer = int(input())
    number1 = answer
    print(" ")
    print("Enter another number")
    answer = int(input())
    number2 = answer
    number3 = number1 / number2
    print(" ")
    print("The answer is")
    print(number3)

def Numbers():
    print("Enter a number")
    answer = int(input())
    number = answer

    while number > 0:
        number = number - 2
    
    if number < 0:
        print(" ")
        print("This number is odd")
    elif number == 0:
        print(" ")
        print("This number is even")

def Voting():
    print("Enter your age")
    answer = int(input())
    age = answer

    if age >= 18:
        print(" ")
        print("You are eligible to vote!")
    else:
        print(" ")
        print("You are not eligible to vote.")

def Equasion():
    # Multiply 5 by 2
    number1 = 5 * 2

    # Add 3
    number2 = number1 + 3

    # Print the amswer (a)
    print(number2)

def Calculator():
    print("Enter a number")
    answer = int(input())
    number1 = answer

    print(" ")
    print("Enter another number")
    answer = int(input())
    number2 = answer

    print(" ")
    print("Enter an arithmetic operation (+, -, *, /)")
    answer = input()
    arithmetic = answer

    if number1 == 0:
        print(" ")
        print("Math Error")
    elif number2 == 0:
        print(" ")
        print("Math error")
    else:
        if arithmetic == "+":
            number3 = number1 + number2
            print(" ")
            print(number3)
        elif arithmetic == "-":
            number3 = number1 - number2
            print(" ")
            print(number3)
        elif arithmetic == "*":
            number3 = number1 - number2
            print(" ")
            print(number3)
        elif arithmetic == "/":
            number3 = number1 - number2
            print(" ")
            print(number3)
        else:
            print(" ")
            print("Syntax Error")


def Name():
    print("What is your name?")
    answer = input()
    name = answer
    print("Welcome", name)

def Numbers2():
    print("Enter a number")
    answer = int(input())
    number1 = answer
    print("Enter another number")
    answer = int(input())
    number2 = answer
    number3 = number1 + number2
    print(number3)

def Colours():
    print("What is your favourite colour?")
    answer = input()
    colour = answer
    print(colour, "good choice!")

def Lines():
    print("Hello")
    print("Hi")

def Format():
    print("Hello, my name is _______, and I'm __ years old")

def Hello():
    runs = 0
    while runs < 5:
        print("Hello")

def Swap():
    V1 = "Hello"
    V2 = 'World'
    print(V1, V2)
    V1 = "World"
    V2 = "Hello"
    print(V1, V2)

def Concentration():
    V1 = "Hello"
    V2 = 'World'
    V3 = V1, V2
    print(V3)

def Initialisation():
    Age = 19
    print(Age)

def Calculator5():
    print("Enter a number")
    answer = int(input())
    number1 = answer
    print(" ")
    print("Enter another number")
    answer = int(input())
    number2 = answer
    number3 = number1 + number2
    number4 = number1 - number2
    number5 = number1 * number2
    number6 = number1 / number2

    print(" ")
    print("The answer is")
    print(number3)
    print(number4)
    print(number5)
    print(number6)
     
def Comparison():
    print("Enter a number")
    answer = int(input())
    number1 = answer
    print(" ")
    print("Enter another number")
    answer = int(input())
    number2 = answer
    if number1 == number2:
        print("These numbers are equal")
    else:
        print("There numbers are not equal")
 
def Strings():
    print("Hello", "World")

def IfElse():
    print("Enter your age")
    answer = int(input())
    age = answer

    if age >= 18:
        print(" ")
        print("You are eligible to vote!")
    else:
        print(" ")
        print("You are not eligible to vote.")

def NestedIf():
    print("Enter a number")
    answer = int(input())
    number1 = answer

    if not number1 == 0:
        if number1 > 0:
            print("This number is positive")
        else:
            print("This number is negative")
    else:
        print("This number is 0")

def Repeat():
    number = 0
    while number > 10:
        number = number + 1
        print(number)

Techtorium()