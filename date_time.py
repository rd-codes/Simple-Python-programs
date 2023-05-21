import time
import datetime

#Python script to display the various Date Time formats.

#a) Current date and time
#b) Current year
#c) Month
#d) Week number 
#e) Day
#f) Day of the month
#g) Day of week

print("The current Date and Time:" , datetime.datetime.now())
print("Year:", datetime.date.today().strftime("%Y"))
print("Month:", datetime.date.today().strftime("%B"))
print("Week No:", datetime.date.today().strftime("%W"))
print("Day of year:", datetime.date.today().strftime("%j"))
print("Day of the month:", datetime.date.today().strftime("%d"))
print("Day of week:", datetime.date.today().strftime("%A"))
