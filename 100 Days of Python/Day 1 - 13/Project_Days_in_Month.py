def is_leap_year(year):
    if year % 4 == 0:
        return True
    elif year % 100 == 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        False

def no_of_days(year, month):
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month == 2 and is_leap_year(year):
        return 29
    else:
        return days_in_months[month - 1] 
    

year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

days = no_of_days(year, month)
print(days) 