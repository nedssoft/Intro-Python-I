"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

cal = calendar.Calendar(firstweekday=6)
td = datetime.today()

def print_calendar(cal):
  for c in cal:
    print(c)

def print_usage_statement():
   print('Ensure the input format is correct\nThe correct format is month year, or month only, example 2 2020 or 2 ')


def get_calendar():
  # get the commandline args
  inputs = sys.argv[1:]
  count = len(inputs)
  if count and count > 1:
    month, year = inputs[0], inputs[1]
    if (int(month) <= 12 and year):
      return print(cal.monthdayscalendar(int(year), int(month))) 
    else:
      return print_usage_statement()
  elif (count ==1):
    month = inputs[0]
    if (int(month) <= 12):
      return print(cal.monthdayscalendar(td.year, int(month)))
    else:
      return print_usage_statement()
  else:
    return cal.monthdayscalendar(td.year, td.month)
  
get_calendar()


