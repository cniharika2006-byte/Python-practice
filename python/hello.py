print("hello world")

name="niharika"
age=19
cgpa=9.0
d=True
print(name,cgpa,age,d)

print(type(name))
print(type(age))
print(type(cgpa))
print(type(d))

import keyword
print(keyword.kwlist)

a=bin(10)
print(a)
print(id(a))
print(type(id(a)))#binary

a=oct(500)
print(a)
print(type(a))#octa decimal

a=hex(11)
print(a)
print(type(a))#hexa decimal

r=10
for i in range(r):
    print(i)#for range datatype    range()

#area of the rectangle
l=int(input("enter the lenth of rectanle:"))
b=int(input("enter breadth of rectangle:"))
area=l*b
print("area of rectangle:",area)

