"""
Exercise:
Write a program that creates a datetime object for November 4, 2020 , 14:53:00. The object created should call the strftime method with the appropriate format to display the following result:

2020/11/04 14:53:00
20/November/04 14:53:00 PM
Wed, 2020 Nov 04
Wednesday, 2020 November 04
Weekday: 3
Day of the year: 309
Week number of the year: 44
expected output

Note: Each result line should be created by calling the strftime method with at least one directive in the format argument.

"""

from datetime import datetime


dt = datetime(2020, 11, 4, 14,53,00)
print(dt.strftime("%Y/%m/%d %H:%M:%S"))
print(dt.strftime("%y/%B/%d %H:%M:%S %p"))
print(dt.strftime("%a, %Y %b %d"))
print(dt.strftime("%A, %Y %B %d"))
print(dt.strftime("Weekday: %w"))
print(dt.strftime("Day of the year: %j"))
print(dt.strftime("Week number of the year: %W"))