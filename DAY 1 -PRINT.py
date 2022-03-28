print("welcome to the Roller-coaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the roller-coaster")
    age = int(input("How old are you? "))
    if age >= 18:
        print("Your ticket fee is $12")
    elif age >= 12 < 18:
        print("Your ticket fee is 7$")
    elif age <= 8:
        print("you can ride the roller-coaster for free")
    else:
        print("Your ticket fee is $5")
elif height < 80:
    print("You're way too small to ride a roller-coaster")
else:
    print("Sorry, you'd have to grow taller before you can ride")
