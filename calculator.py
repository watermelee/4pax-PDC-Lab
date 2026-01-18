# Member 1: add function and loop
def add(a, b):
    return a + b

# Member 2: Subtraction
def subtract(a, b):
    return a - b

#Member 3 : Multiplication
def multiply(a,b):
    return a * b 

# Member 4: Division
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def main():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "5":
            print("Exiting...")
            break
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if choice == "1":
            print("Result:", add(a, b))
        if choice == "2":
            print("Result:", subtract(a, b))
        if choice == "3":
            print("Result:", multiply(a,b))
        if choice == "4":
            print("Result:", divide(a, b))
        

main()