# Find the largest number among three numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a>=b and a>=c :
    largest = a
if b>=a and b>=c:
    largest = b
if c>=a and c>=b:
    largest = c

print(f"The Largest Number is: {largest}")