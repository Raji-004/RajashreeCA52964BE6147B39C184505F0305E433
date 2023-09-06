#1.1 write a program to check if the given year is leap year or not using if elif else statements

def isLeapYear(year):
  if(year % 4 == 0 and year % 100 != 0):
    return True
  elif(year % 400 == 0):
    return True
  else:
    return False

year = int(input("Enter the value: "))
if isLeapYear(year):
  print("{} is a Leap Year.".format(year))
else:
  print("{} is not a Leap Year.".format(year))
  