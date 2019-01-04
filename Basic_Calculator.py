  # List of modes to print
modes = ["Addition(+)", "Subtraction(-)", "Multiplication(*)", "Division(/)"]

  # Define a function called 'calc' that calculates the user input
def calcAddition(x, y):
    print("{} + {} = {}!".format(x, y, x+y))
    input("Program complete, press ENTER to exit~. ")
def calcSubtraction(x, y):
    print("{} - {} = {}!".format(x, y, x-y))
    input("Program complete, press ENTER to exit~. ")
def calcMultiplication(x, y):
    print("{} * {} = {}!".format(x, y, x*y))
    input("Program complete, press ENTER to exit~. ")
def calcDivision(x, y):
    print("{} ÷ {} = {}!".format(x, y, x/y))
    input("Program complete, press ENTER to exit~. ")

  # Print the list of modes
print ("Select mode: ")
for x in modes:
    print (x)

  # Ask the user to select a mode (+, -, *, or /)
select = input()

  # Ask the user what numbers they want to calculate
x = float(input("First number: "))
y = float(input("Second number: "))

  # If user selects +, -, *, or /, calculate x and y together
if select in ["+", "Addition", "addition"]:
    calcAddition(x,y)
elif select in ["-", "Subtraction", "subtraction"]:
    calcSubtraction(x,y)
elif select in ["*", "Multiplication", "multiplication"]:
    calcMultiplication(x,y)
elif select in ["/", "Division", "division"]:
    calcDivision(x,y)

  # If something fucks up, show an error message
else:
    print("An error has occured. Press enter to exit the program.")