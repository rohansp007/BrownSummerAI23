#Task 1: Converting from hours to minutes.

hours_task_1 = float(input("How many hours? "))
print(f'{hours_task_1} hours is {60*hours_task_1} minutes.')

#Task 2: Converting from either hours to minutes or minutes to hours.

user_input = input("Would you like to convert from hours to minutes (input H) or from minutes to hours (input M)? ")
boolean2 = True
while boolean2:
    if user_input == "H":
        hours_task_2 = float(input("How many hours? "))
        print(f'{hours_task_2} hours is {60*hours_task_2} minutes.')
        boolean2 = False
    elif user_input == "M":
        minutes = float(input("How many minutes?"))
        print(f'{minutes} minutes is {minutes/60} hours.')
        boolean2 = False
    else:
        user_input = input("Would you like to convert from hours to minutes (input H) or from minutes to hours (input M)? ")

#Task 3: Returning the number of characters in a string.

input_string = input("What string would you like to type? ")
print(f'The length of the string is {len(input_string)} characters long.')