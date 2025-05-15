#1. Python program to check leap year.

     
def is_leap_year(year):
    # Leap year is divisible by 4
    # Except years divisible by 100, unless also divisible by 400
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
# Input from user
year = int(input("Enter a year: "))
# Check and print result
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")



#2.Python Program to Find the Largest Among Three Numbers.

    
# Input three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
# Find the largest number
largest = max(num1, num2, num3)
# Print the result
print("The largest number is:",largest)

#3. Python Program to Check if a Number is Positive, Negative or 0.

     
# Input a number
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")
