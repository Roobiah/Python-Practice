print("Welcome to the BMI calculator!")
Weight = float(input("Enter your weight in Kg: "))
Height = float(input("Enter your height in m: "))
BMI = Weight / Height ** 2
new_BMI = round(BMI)
if new_BMI < 18.5:
    print(f"Your BMI is {new_BMI} and you're underweight")
elif new_BMI < 25:
    print(f"Your BMI is {new_BMI} and you have a normal weight ")
elif new_BMI < 30:
    print(f"Your BMI is {new_BMI} and you are overweight")
elif new_BMI < 35:
    print(f"Your BMI is {new_BMI} and you are obese")
else:
    print(f"Your BMI is {new_BMI} and you are clinically obese")
