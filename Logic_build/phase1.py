# Take a number and print whether it’s positive, negative, or zero
num = int(input("enter the no. : "))
if num > 0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")


# Check if a number is even or odd
if num % 2 == 0:
    print("even")
else:
    print("odd")


# Check if a given year is a leap year
year = int(input("enter the year : "))
if year % 400 == 0:
    print("its a leap year ")
elif year % 100 == 0:
    print("its a not a leap year ")
elif year % 4 == 0 and year % 100 != 0:
    print("its a leap year ")
else:
    print("its a not a leap year ")


# Take three number and print the largest 
a = int(input("enter the no.a : "))
b = int(input("enter the no.b : "))
c = int(input("enter the no.c : "))
if a>b and a>c:
    print("a is largest")
elif b>a and b>c:
    print("b is largest")
elif c>a and c>b:
    print("c is largest")
else:
    print("a,b,c are equall")


# Take a character and check whether it is vowel or consonant
character = input("enter the character : ")
vowel = ['a','e','i','o','u','A','E','I','O','U']
if character in vowel:
    print("its a vowel")
else:
    print("its a consonant")

# Take a character and check whether it’s uppercase, lowercase, a digit, or a special character
if character == character.upper():
    print("its uppercase")
elif character == character.lower():
    print("its lowercase")
elif character.isdigit():
    print("its a digit")
else:
    print("its a special character")


# Take three sides and check if they form a valid triangle
if a+b > c:
    print("triangle is valid")
elif b+c > a:
    print ("triangle is valid")
elif c+a>b:
    print("triangle is valid")
else:
    print("trinangle is invalid")


# If the sides form a valid triangle, determine whether it is equilateral, isosceles, or scalene
if a==b==c:
    print("triangle is equilateral")
elif a == b or b == c or a == c:
    print ("triangle is isosceles")
else:
    print("trinangle is scalene")


# Take a month number (1–12) and print the number of days in that month (ignore leap years)
# Take a day number (1–7) and print the corresponding day name
# Take a 3-digit number and check if all digits are distinct
# Take coordinates (x, y) and determine which quadrant the point lies in
# Check whether a number is a perfect square (without using the square root function).
# Take a 3-digit number and determine if the middle digit is the largest, smallest, or neither
# Take a number and print “Fizz” if divisible by 3, “Buzz” if divisible by 5, and “FizzBuzz” if divisible by both
# Take three numbers and print the median value (neither maximum nor minimum)
# Take electricity units consumed and calculate the bill as per slabs (using if-else)
# Take a password string and check basic rules (length ≥ 8 and contains at least one digit)
# Take three numbers and check if they can form a Pythagorean triplet
