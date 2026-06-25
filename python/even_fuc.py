def square(n):
    return n*n
print(square(5))


def add(a,b):
    return a+b
print(add(1,2))


def check(n):
    if n%2==0:
     return "even"
    else:
     return "odd"
print(check(1))


def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
print(sum_n(5))#1+2+3+4+5