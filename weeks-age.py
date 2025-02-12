age = int(input ("what's your current age? "))

#noob bodn :
#days = int(365 * 90)
#weeks = int(52 * 90)
#month = int(12 * 90)

#khob bood vali niaz nabood :
#days, weeks, month = (365*90), (52*90), (12*90)

#ezafe : 
#rest_days = days - age * 365 
#rest_weeks = weeks - age * 52
#rest_month = month - age * 12

rest_years = 90 - age
rest_days = rest_years * 365
rest_weeks = rest_years * 52
rest_month = rest_years * 12

print (f"you have {rest_days} days, {rest_weeks} weeks, and {rest_month} month left. ")