print("Welcome to the love calculator!")
name1 = input("What is your name? ").lower()
name2 = input("What is your partner's name? ").lower()
All_name = name1 + name2
T = All_name.count("t")
R = All_name.count("r")
U = All_name.count("u")
E = All_name.count("e")
L = All_name.count("l")
O1 = All_name.count("o")
V = All_name.count("v")
E2 = All_name.count("e")
TRUE = T + R + U + E
LOVE = L + O1 + V + E2
TRUELOVE = str(TRUE) + str(LOVE)
RESULT = int(TRUELOVE)
if RESULT < 10 or RESULT > 90:
    print(f"Your score is {RESULT}, you go together like coke and mentos")
elif 40 < RESULT < 50:
    print(f"Your Score is {RESULT}, you are alright together")
else:
    print(f"Your score is {RESULT}. ")
