#variables
result = 0.0
loop = True
results = []
average = 0.0

#menu print
print("Current Result: " + str(result))
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

#logic loop
while loop == True:
    menuSelect = int(input("Enter Menu Selection: "))
    
    if not -1 < menuSelect < 8:
        print("Error: Invalid selection!")
    
    if menuSelect == 0:
        print("Thanks for using this calculator. Goodbye!")
        loop = False
        quit()
        
    if menuSelect == 1:
        op = input("Enter first operand: ")
        op2 = input("Enter second operand: ")
        print("")
        result = float(op) + float(op2)
        print("Current Result: " + str(result))
        results.append(result)
        
    if menuSelect == 2:
        op = input("Enter first operand: ")
        op2 = input("Enter second operand: ")
        print("")
        result = float(op) - float(op2)
        print("Current Result: " + str(result))
        results.append(result)
    
    if menuSelect == 3:
        op = input("Enter first operand: ")
        op2 = input("Enter second operand: ")
        print("")
        result = float(op) * float(op2)
        print("Current Result: " + str(result))
        results.append(result)
        
    if menuSelect == 4:
        op = input("Enter first operand: ")
        op2 = input("Enter second operand: ")
        print("")
        result = float(op) / float(op2)
        print("Current Result: " + str(result))
        results.append(result)
        
    if menuSelect == 5:
        op = input("Enter first operand: ")
        op2 = input("Enter second operand: ")
        print("")
        result = float(op) ^ float(op2)
        print("Current Result: " + str(result))
        results.append(result)
        
    if menuSelect == 6:
        op = input("Enter first operand: ")
        op2 = input("Enter second operand: ")
        print("")
        result = math.log(op2,op)
        print("Current Result: " + str(result))
        results.append(result)
        
    if menuSelect == 7:
        if len(results) == 0:
            print("Error: no calculations yet to average!")
            print("")
        else:
            result = 0.0
            for f in results:
                result += f
            average = result / len(results)
            print("")
            print("Sum of calculations: " + str(result))
            print("Number of calculations: " + str(len(results)))
            print("Average of calculations: " + str(average))