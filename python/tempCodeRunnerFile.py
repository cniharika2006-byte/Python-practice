print("-----SMART CALCULATOR-----")
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
   if a/a==0:
    print("prime")
   else:
    print("not prime")