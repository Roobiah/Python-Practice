print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[Treasure]
*******************************************************************************
''')
print("Welcome to the treasure island!\nYour mission is to find the treasure..Enjoy")
step1 = input("Which side do you want to go? Left or Right? ").lower()
if step1 == 'left':
    print("You're at the river bank")
    step2 = input("Do you want to swim or wait? ").lower()
    if step2 == 'wait':
        print("Your boat is here...Let's go")
        step3 = input("Which entrance door would you prefer? Blue, Red or Yellow ").lower()
        if step3 == 'blue':
            print("Congratulations!!! You've found the treasure")
        elif step3 == 'red':
            print("Danger Zone!!! You are caught up in a trap\nGame Over")
        else:
            print("Unfortunately, you entered a wrong room\nGame Over")
    else:
        print("Oops,You've been eaten up by a shark...\nGame Over!")
else:
    print("Oops! You're in a thick forest..it's the wrong way\nGame Over!")
