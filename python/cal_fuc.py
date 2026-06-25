def mini_calculator(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    squ=a**2
    mod=a%b     #remainder
    quo=a//b
    maximum=max(a,b)
    avg=(a+b)/2
    print(add,sub,mul,div,squ,mod,quo,maximum,avg,)
mini_calculator(1,3)


#inputs from user
def mini_calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "avg":
        return (a + b) / 2
    elif operation == "mul":
        return a * b
    else:
        return "Invalid operation"

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operation (add/sub/avg/mul): ")

print(mini_calculator(a, b, op))
 