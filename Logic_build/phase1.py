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
character = input("Enter the character: ")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
if character.isalpha():
    if character in vowels:
        print("It's a vowel")
    else:
        print("It's a consonant")
else:
    print("It's neither a vowel nor a consonant")

# Take a character and check whether it’s uppercase, lowercase, a digit, or a special character
if character == character.isupper():
    print("its uppercase")
elif character == character.islower():
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
month =int(input("enter the month no. : "))
if month ==1:
    print("it has 31 days")
elif month==2:
    print("it has 28 days")

while month>=3 and month<=7:
    if month % 2 == 0 :
        print("it has 30 days")
        break
    else:
        print("it has 31 days")
        break

while month>7 and month<=12:
    if month % 2 ==0:
        print("it has 31 days")
        break
    else:
        print("it has 30 days")
        break


# Take coordinates (x, y) and determine which quadrant the point lies in
x =int(input("enter the x_coordinate : "))
y =int(input("enter the y_coordinate : "))
if x>0 and y>0:
    print("point is in first quadrant")
elif x>0 and y<0:
    print("point is in second quadrant")
elif x<0 and y>0:
    print("point is in fourth quadrant")
elif x<0 and y<0:
    print("point is in third quadrant")
elif x==0 and y==0:
    print("point is at origin")
else:
    print("point are wrong entered")

# Check whether a number is a perfect square (without using the square root function).
num = int(input("Enter the number: "))

found = False

for i in range(num + 1):
    if i * i == num:
        print("It's a perfect square")
        found = True
        break

if not found:
    print("It's not a perfect square")


# Take a password string and check basic rules (length ≥ 8 and contains at least one digit)
password = input("enter the password : ")

# Check basic password rules (length >= 8 and contains at least one digit)
if len(password) >= 8 and any(ch.isdigit() for ch in password):
    print("Password is valid")
else:
    print("Password is invalid")
