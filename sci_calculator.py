#imports
import math

#variables. All results from the calculations are stured in results[] at the end of each operation
result = 0.0
loop = True
results = []
average = 0.0
print("Current Result: " + str(result))

#print the menu in a function
def print_menu():
    print("")
    print("Calculator Menu")
    print("---------------")
    print("0. Exit Program")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Logarithm")
    print("7. Display Average")

print_menu()

#logic loop
while loop == True:
    #prompt menu selection (repeated many times)
    menuSelect = int(input("Enter Menu Selection: "))
    
    #check if selection is valid
    if not -1 < menuSelect < 8:
        print("Error: Invalid selection!")
    
    #quit option
    if menuSelect == 0:
        print("Thanks for using this calculator. Goodbye!")
        loop = False
        quit()
        
    #simple addition
    if menuSelect == 1:
        op = input("Enter first operand: ")
        op2 = input("Enter second operand: ")
        print("")
        result = float(op) + float(op2)
        print("Current Result: " + str(result))
        print_menu()
        results.append(result)
        
    #subtraction
    if menuSelect == 2:
        op = input("Enter first operand: ")
        op2 = input("Enter second operand: ")
        print("")
        result = float(op) - float(op2)
        print("Current Result: " + str(result))
        print_menu()
        results.append(result)
    
    #multiplication
    if menuSelect == 3:
        op = input("Enter first operand: ")
        op2 = input("Enter second operand: ")
        print("")
        result = float(op) * float(op2)
        print("Current Result: " + str(result))
        print_menu()
        results.append(result)
        
    #division
    if menuSelect == 4:
        op = input("Enter first operand: ")
        op2 = input("Enter second operand: ")
        print("")
        result = float(op) / float(op2)
        print("Current Result: " + str(result))
        print_menu()
        results.append(result)
        
    # exponent (remember not to use ^)
    if menuSelect == 5:
        op = input("Enter first operand: ")
        op2 = input("Enter second operand: ")
        print("")
        if str(op2) == "RESULT":
            result = int(op) ** result
        else:
            result = int(op) ** int(op2)
        print("Current Result: " + str(result))
        print_menu()
        results.append(result)
        
    #math.log... the import is used here
    if menuSelect == 6:
        op = input("Enter first operand: ")
        op2 = input("Enter second operand: ")
        print("")
        result = math.log(float(op2),float(op))
        print("Current Result: " + str(result))
        print_menu()
        results.append(result)
        
    #average. the list of results[] is used extensively here
    if menuSelect == 7:
        if len(results) == 0:
            print("Error: No calculations yet to average!")
            print("")
        else:
            result = 0.0
            for f in results:
                result += f
            average = round(result / len(results), 2)
            print("")
            print("Sum of calculations: " + str(result))
            print("Number of calculations: " + str(len(results)))
            print("Average of calculations: " + str(average))