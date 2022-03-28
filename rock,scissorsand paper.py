import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
available_choices = [rock, paper, scissors]

choice = int(input("What do you want to choose: Type 0 for rock, 1 for scissors and 2 for paper: "))
if choice >= 3 or choice < 0:
    print("You've typed an invalid number, you lose")
else:
    print(available_choices[choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(available_choices[computer_choice])
    if choice == 0 and computer_choice == 2:
        print("You lose")
    elif choice == 2 and computer_choice == 0:
        print("You win")
    elif choice > computer_choice:
        print("You win")
    elif choice < computer_choice:
        print("You lose")
    elif choice == computer_choice:
        print("You draw")
    else:
        print("You lose")
