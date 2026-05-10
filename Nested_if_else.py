# 1. A theme park has these rules: 
# You can ride the roller coaster if you are at least 12 years old AND at least 140 cm tall. Write the if-else code for this.

age = 12
height = 140
if age >= 12 and height >= 140:
    print("You can ride the roller coaster!")
else:
    print("Sorry, you cannot ride the roller coaster.")

# 2. Design a Traffic Light System. 
# Given a variable light that can be "red", "yellow", or "green", print the correct instruction. 
# Also handle an invalid color with an error message.

light = input("Enter traffic light color : ")
if light == "red":
    print("Stop")
elif light == "yellow":
    print("Get ready to go")
elif light == "green":
    print("Go")
else:
    print("Invalid traffic light color!")

# 3. Write a match statement that takes a number 1-4 and 
# prints the corresponding season: 1=spring, 2-summer, 3-autumn, 4-winter. Default: "unknown".
number = int(input("Enter a number : "))
match number:
    case 1:
        print("Spring")
    case 2:
        print("Summer")
    case 3:
        print("Autumn")
    case 4:
        print("Winter")
    case _:
        print("Unknown season")

# 4. Write a login system using nested if. Check:
# ➤ If username equals "admin"
# ➤ Inside that, if password equals "pass123"
# Print appropriate messages for: valid login, wrong password, wrong username.

username = input("Enter username : ")
if username == "admin":
    password = input("Enter password : ")
    if password == "pass123":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")

# 5. Design a Bank Loan Approval System. Approve a loan only if ALL three conditions are met: ➤ Age is between 21 and 60 (inclusive)
# ➤ Monthly income is at least 30,000
# ➤ Credit score is at least 700
# If not approved, print which condition failed. If multiple fail, pick the most important one to report.

age = int(input("Enter age: "))
income_monthly = int(input("Enter monthly income: "))
credit_score = int(input("Enter credit score: "))

verify_age    = 21 <= age <= 60
verify_income = income_monthly >= 30000
verify_credit = credit_score >= 700

if verify_age and verify_income and verify_credit:
    print("Loan Approved")
else:
    if not verify_age:
        print("Age must be between 21 and 60")
    elif not verify_income:
        print("Income must be at least 30,000")
    else:
        print("Credit score must be at least 700")



# 6. You are developing a simple ticket booking system for a movie theatre. 
# The ticket price depends on the age of the person and whether they have a membership card. 
# If the person is under 12, the ticket is free. If the person is between 12 and 60: If they have a membership card, 
# the ticket costs Rs. 150. If not, the ticket costs Rs. 200. If the person is above 60, they get a senior citizen discount, 
# and the ticket costs Rs. 100. Write a Python program using nested if-else to calculate 
# and print the ticket price based on the user's age and membership
# status.

age = int(input("Enter age: "))
membership = input("Do you have a membership card? (yes/no): ").lower()

if age < 12:
    print("The ticket is free.")
elif 12 <= age <= 60:
    if membership == "yes":
        print("The ticket costs Rs. 150.")
    else:
        print("The ticket costs Rs. 200.")
else:
    print("The ticket costs Rs. 100.")


# 7. A company decided to give bonus of 5% to employee if his/her year of service is more than 5years. 
# Ask user for their salary and year of service and print the net bonus amount.

salary=float(input("Enter your salary: "))
service=int(input("Enter your years of service: "))

if service > 5:
    bonus_salary = salary * 0.05 + salary
    print(f"Your bonus amount is: Rs. {bonus_salary}")
else:
    print("Sorry, you are not eligible for a bonus.")

# 8. Write a python program which accepts the radius of circle from user and compute the area.

radius = float(input("Enter the radius of the circle: "))
area = 3.14 * radius ** 2
print(f"The area of the circle is: {area}")



# 9. Accept the age, gender ('M', 'F'), number of days and display the wages accordingly.

age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()
days = int(input("Enter number of days: "))

if age >=18 and age<30 and gender=="M":
    print(f"Wages: Rs. {days * 700}")
elif age >=18 and age<30 and gender=="F":
    print(f"Wages: Rs. {days * 750}")
elif age >=30 and age<40 and gender=="M":
    print(f"Wages: Rs. {days * 800}")
elif age >=30 and age<40 and gender=="F":
    print(f"Wages: Rs. {days * 850}")




# 10. Accept input from user
# If given number is a multiple of both 3 and 5 prints "Fizz Buzz" instead of number
# If given number is a multiple of 3 but not 5 prints "Fizz" instead of number
# If given number is a multiple of 5 but not 3 prints "Buzz" instead of number
# If given number is not multiple of 3 or 5 prints value as usual.

number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)



#