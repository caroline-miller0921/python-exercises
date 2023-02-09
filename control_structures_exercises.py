
# 1. Conditional Basics

# a. prompt the user for a day of the week, print out whether the day 
# is Monday or not

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_of_the_week = input('Please enter a day of the week: ')
if day_of_the_week == 'Monday':
    print('The day you entered is Monday')
elif day_of_the_week in days_of_week and day_of_the_week != 'Monday':
    print('You have entered a day of the week which is not Monday')
elif day_of_the_week not in days_of_week:
    print('This is not a day of the week!')

# b. prompt the user for a day of the week, print out whether the day is 
# a weekday or a weekend 


days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_of_the_week = input('Please enter a day of the week: ')
if day_of_the_week in ['Saturday', 'Sunday']:
    print("Whoohoo! It's the weekend!")
elif day_of_the_week in days_of_week and day_of_the_week not in ['Saturday', 'Sunday']:
    print('It is a weekday!')
elif day_of_the_week not in days_of_week:
    print('This is not a day of the week!')
         


