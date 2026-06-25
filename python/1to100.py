for i in range(1,101):
   print(i)

#Check whether a number is positive, negative, or zero.
num=int(input("enetr a no.:"))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")

#print even no. from 1 to 100
for i in range(1,101):
   if i%2==0:
       print(i)

#COUNTING DIGITS IN A NO.
num=int(input("enter a no.:"))
count=0
while num>0:
    count+=1
    num=num//10
print(count)

#REVERSING A NO.
num=int(input("enter a no.:"))
reverse=0
while num>0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed number:", reverse)