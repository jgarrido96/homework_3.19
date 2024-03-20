
# 1. Decisions at the Crossroad

# Task 1: Code Correction
'''
number = int(input("Enter a number: "))
if number > 0:
    print("Then number is prositive.")
elif number == 0:
    print("The number is zero")
else:
    print("The number is negative")
    '''
print("\n")
'''
# 2. The Greatest Showdown

# Task 1: Identify the Smallest

user_input_1 = int(input("Pick a number! "))
user_input_2 = int(input("Pick another "))
user_input_3 = int(input("Heck, pick one more. "))
output_1 = ("The biggest number is ")
output_2 = ("The smallest number is ")
print("\n")
if user_input_1 > user_input_2 and user_input_3:
    print(output_1 + str(user_input_1))
elif user_input_2 > user_input_1 and user_input_3:
    print(output_1 + str(user_input_2))
elif user_input_3 > user_input_1 and user_input_2:
    print(output_1 + str(user_input_3))

# Task 2: Identify the Smallest

if user_input_1 < user_input_2 and user_input_3:
    print(output_2 + str(user_input_1))
elif user_input_2 < user_input_1 and user_input_3:
    print(output_2 + str(user_input_2))
elif user_input_3 < user_input_1 and user_input_3:
    print(output_2 + str(user_input_3))

# Task 3: Equality Check


output_3 = "Your first two numbers matched, "
output_4 = "Your last two numbers matched, "
output_5 = "Your first and last numbers matched, "
high = "and were the highest!"
low = "and were the lowest!"
if user_input_1 == user_input_2 or user_input_3:
    if user_input_1 == user_input_2 > user_input_3:
        print(output_3 + high)
    elif user_input_1 == user_input_2 < user_input_3:
        print(output_3 + low)
    elif user_input_1 == user_input_3 < user_input_2:
        print(output_5 + low)
    elif user_input_1 == user_input_3 > user_input_2:
        print(output_5 + high)
if user_input_2 == user_input_3:
    if user_input_2 == user_input_3 > user_input_1:
        print(output_4 + high)
    elif user_input_2 == user_input_3 < user_input_1:
        print(output_4 + low)

'''
print("\n")

# 3. Leap Year Explorer

year_input = int(input("Input a year! "))
if year_input % 400 == 0:
    print("This is a very special leap year!")
elif year_input % 100 == 0:
    print("This is surprisingly not a leap year!")
elif year_input % 4 == 0:
    print("This is definitely a leap year!")
else:
    print("This is not a leap year. :(")


