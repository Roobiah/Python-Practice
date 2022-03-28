import random
names_string = input("Give the names of everyone separated by a comma. ")
names = names_string.split(",")
'''
no_of_names = len(names)
random_name = random.randint(0, no_of_names - 1)
the_name = (names[random_name])
print(f"{the_name} is paying the bill for today!")
'''
the_name = random.choice(names)
print(the_name + " is paying the bill for today")
