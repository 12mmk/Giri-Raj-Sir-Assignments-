weight = float(input("Enter your weight in decimal value: "))
height = float(input("Enter your height in decimal value: "))
bmi = weight / (height ** 2)
status_weight = {
    "Underweight": bmi < 18.5,
    "Normal weight": 18.5 <= bmi < 25,
    "Overweight": 25 <= bmi < 30,
    "Obesity": bmi >= 30
}

print(f'Weight: {weight} kg')
print(f'Height: {height} m')
print(f'BMI: {bmi:.2f}')