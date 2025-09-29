print("********** Calculator **********")

# defining functions
def calculation():
    firstNum = float(input("Enter first number: "))
    secondNum = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, /, *): ")
    if operation == '+':
        result = firstNum + secondNum
    elif operation == '-':
        result = firstNum - secondNum
    elif operation == '/':
        if secondNum == 0:
            return print("Error: Division by zero\n")
        else:
            result = firstNum / secondNum
    elif operation == '*':
        result = firstNum * secondNum
    else:
        return print("Invalid operation\n")
    return print(f"The result is: {result}")



def even_odd():
    num = int(input("Enter a number: "))
    if num >=0:
        if num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")
    else:
        print("Please enter a non-negative integer\n")   
        
        
def percentage():
    totalNum = int(input("Enter total number: "))
    obtainedNum = int(input("Enter obtained number: "))
    percent = (obtainedNum / totalNum) * 100
    print(f"The percentage is: {percent}%")           

while True:
    print("1 for operations(+, -, /, *)\n")
    print("2 to check even/odd\n")
    print("3 to calculate percentage\n")
    print("4 to switch off\n")

    option = input("Choose an option: ")
    if option == '1':
        calculation()  
    elif option == '2':
        even_odd()
    elif option == '3':
        percentage()
    elif option == '4':
        print("Calculator switched off")
        break  
    else:
        print("Invalid option\n")
        
                
        



