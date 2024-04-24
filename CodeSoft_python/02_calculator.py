def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y
def mod(x,y):
    return x%y

def main():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulous(%)")

    # Prompt user to input two numbers and operation choice
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        choice = input("Enter operation choice (1/2/3/4/5): ")

        if choice not in ['1', '2', '3', '4','5']:
            print("Invalid choice! Please enter a valid operation choice.")
            return

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice=='5':
            print("Result:", mod(num1,num2))
            
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

if __name__ == "__main__":
    main()
