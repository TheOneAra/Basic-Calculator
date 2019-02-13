  # List all the modes available to print
modes = ["1. Addition(+)", "2. Subtraction(-)", "3. Multiplication(*)", "4. Division(/)", "5. Power(^)"]

  # Define a function that asks if the user wants to use the calculator again
def another():
    another = input("Solve another equation? (Y/N)\n")
    while another in "y" "Y":
        mainCalc()
        break
    else:
        input("Program complete! Press ENTER to exit. ")

  # Define a function called 'calc____' that calculates the user input depending on the mode selected
def calcAddition(x, y):
    print("{} + {} = {}!".format(x, y, x+y))
    another()
def calcSubtraction(x, y):
    print("{} - {} = {}!".format(x, y, x-y))
    another()
def calcMultiplication(x, y):
    print("{} * {} = {}!".format(x, y, x*y))
    another()
def calcDivision(x, y):
    print("{} ÷ {} = {}!".format(x, y, x/y))
    another()
def calcPower(xpow, ypow):
    print("{} to the power of {} = {}!".format(xpow, ypow, pow(xpow,ypow)))
    another()

  # Define a function "mainCalc" that holds the main function of the calculator
def mainCalc():
  # Print the list of modes    
    print ("Select mode: ")
    for x in modes:
        print (x)

  # Ask the user to select a mode (+, -, *, /, or ^)
    select = input()

  # If the user selects one of the modes, ask the user what numbers they want to calculate, then calculate the two numbers
    if select in ["+", "Addition", "addition", "1"]:
        x = float(input("First number: "))
        y = float(input("Second number: "))
        calcAddition(x,y)
    elif select in ["-", "Subtraction", "subtraction", "2"]:
        x = float(input("First number: "))
        y = float(input("Second number: "))
        calcSubtraction(x,y)
    elif select in ["*", "Multiplication", "multiplication", "3"]:
        x = float(input("First number: "))
        y = float(input("Second number: "))
        calcMultiplication(x,y)
    elif select in ["/", "Division", "division", "4"]:
        x = float(input("First number: "))
        y = float(input("Second number: "))
        calcDivision(x,y)
    elif select in ["^", "Power", "power", "5"]:
        xpow = float(input("Number: "))
        ypow = float(input("Power: "))
        calcPower(xpow, ypow)

  # If something fucks up, show an error message
    else:
        input("An error has occured. Press ENTER to exit.")
        
mainCalc()
