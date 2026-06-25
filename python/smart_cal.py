print("-----SMART CALCULATOR-----")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Factorial")
print("6. Prime Check")
choice = int(input("Enter choice: "))
a=int(input("ENTER A VALUE:"))
b=int(input("ENETR B VALUE:"))
def add(a,b):
    return a+b
print(add(a,b))
def sub(a,b):
    return a-b
print(sub(a,b))
def mul(a,b):
    return a*b
print(mul(a,b))
def div(a,b):
    return a/b
print(div(a,b))
def fact(a):
  fact = 1
  for i in range(1, a + 1):
   fact = fact * i
  return fact
print(fact(a))
def prime(a):
    if a < 2:
       return False
    for i in range(2, a):
      if a % i == 0:
        return False

    return True
if choice == 1:
    print(add(a,b))
elif choice == 2:
    print(sub(a,b))
elif choice == 3:
    print(mul(a,b))
elif choice == 4:
    print(div(a,b))
elif choice == 5:
    print(fact(a))
elif choice == 6:
    if prime(a):
        print("Prime")
    else:
        print("Not Prime")