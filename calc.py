def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "cant divide by zero "
    return x/y
while True:
    print("options:")
    print("enter 'add' for addition")
    print("enter 'subtract' for subtraction")
    print("enter 'multiply' for multiplication")
    print("enter 'divide' for division")
    print("enter 'exit' to end the program")

    choice = input("Enter choice: ")
    
    if choice in ['add','subtract','multiply','divide']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == 'add':
            print("Result: ", add(num1, num2))
        elif choice == 'subtract':
            print("Result: ", subtract(num1, num2))
        elif choice == 'multiply':
            print("Result: ", multiply(num1, num2))
        elif choice == 'divide':
            print("Result: ", divide(num1, num2))
    elif choice == 'exit':
            print("Goodbye!")
            break
    else:
        print("Invalid choice")

