
'''
-------------------------------------------------------------------------
Name:		minutes_days.py
Purpose: Enter a number of minutes, and that will calculate
the number of days, hours and minutes that represents 


Author:	Chan. A

Created:	date in 12/03/2020
-------------------------------------------------------------------------
'''
minute = float(input("Enter number of minutes: "))

day = minute // (1440)
minute = minute % (1440)

hour = minute // 60
minute = minute % 60

minutes = minute // 1
print("Day(s): ", day, "\nHour(s): ", hour, "\nMinute(s): ", minutes)