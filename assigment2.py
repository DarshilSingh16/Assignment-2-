# Task 1

a = int(input("Enter a number :"))

if(a%2==0):
    print(a,"is a even number")
else:
    print(a,"is a odd number")

#task 2

total = 0
for i in range(1, 51):
    total += i

print("Sum of numbers from 1 to 50 is:", total)