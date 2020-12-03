'''
-------------------------------------------------------------------------
Name:		days_hours.py
Purpose: lets you enter a number of hours, and that converts it to days and hours

Author:	Chan. A

Created:	date in 12/03/2020
-------------------------------------------------------------------------
'''
hours = int(input("Enter number of hours: "))

days = hours//24

extra_hours = hours%24

print(str(hours) + " hours = " + str(days) + " and " + str(extra_hours) + " hours.")