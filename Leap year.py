year = int(input("Which year do you want to check? "))
first_test = year % 4
second_test = year % 100
third_test = year % 400
if first_test != 0:
    print("Not a leap year")
elif second_test != 0:
    print("leap year")
elif third_test == 0:
    print("leap year")
else:
    print("Not a leap year")
