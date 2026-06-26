print("-----SMART CALCULATOR-----")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Factorial")
print("6. Prime Check")
print("7. Exit")
choice = int(input("Enter choice: "))
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def fact(a):
    fact = 1
    for i in range(1, a + 1):
        fact *= i
    return fact
def prime(a):
    if a < 2:
        return False
        
    for i in range(2, a):
        if a % i == 0:
            return False
    return True
if choice == 1:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Answer =", add(a, b))
elif choice == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Answer =", sub(a, b))
elif choice == 3:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Answer =", mul(a, b))
elif choice == 4:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Answer =", div(a, b))
elif choice == 5:
    a = int(input("Enter a number: "))
    print("Factorial =", fact(a))
elif choice == 6:
    a = int(input("Enter a number: "))
    if prime(a):
        print("Prime")
    else:
        print("Not Prime")
elif choice == 7:
    print("Thank you for using Smart Calculator!")
else:
    print("Invalid Choice")
