while True:
    g = int(input("Enter the first number : "))
    h = int(input("Enter the second number : "))
    op = input("Enter +, -, *, /, %, percent for the specific operation : ")
    def sum(g,h):
        return g+h
    def diff(g,h):
        return g-h
    def prod(g,h):
        return g*h
    def div(g,h):
        return g/h
    def even_check(g):
        if g%2==0:
            return "First number is even"
        else:
            return "First number is odd"
    def percent(g,h):
        return (g/h)*100
    if op == "+":
        result = sum(g,h)
    elif op == "-":
         result = diff(g,h)
    elif op == "*":
         result = prod(g,h)
    elif op == "/":
        result = div(g,h)
    elif op == "%":
        result = even_check(g)
    elif op == "percent":
        result = percent(g,h)
    else:
        print("Invalid operation entered!")
        continue
    print("The result of given numbers is : " , result)
    cnt = input("Do You wish to continue another operation? (Yes/No) : ")
    if cnt != "Yes":
        print("Thanks for using the program, it will now exit!")
        break
    else:
        continue