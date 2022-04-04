def is_leap(test_year):
    first_test = test_year % 4
    second_test = test_year % 100
    third_test = test_year % 400
    if first_test != 0:
        return False
    elif second_test != 0:
        return True
    elif third_test == 0:
        return True
    else:
        return False


def days_in_month(test_year, test_month):
    if test_month > 12 or test_month < 1:
        return 'Invalid Month'
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(test_year) and test_month == 2:
        return 29
    return month_days[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
