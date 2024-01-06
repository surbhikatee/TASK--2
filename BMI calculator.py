def calculate_bmi(height, weight):
    return weight / (height / 100) ** 2


height=float(input("enter the height in cm:"))
weight=float(input("enter weight in kg:"))

bmi = calculate_bmi(height, weight)
print(f"Your BMI is {bmi}")

if bmi <= 18.4:
       print("You are underweight.")
elif 18.5 <= bmi <= 24.9:
       print("You are healthy.")
elif 25 <= bmi <= 29.9:
       print("You are overweight.")
elif 30 <= bmi <= 34.9:
       print("You are severely overweight.")
elif 35 <= bmi <= 39.9:
       print("You are obese.")
else:
       print("You are severely obese.")