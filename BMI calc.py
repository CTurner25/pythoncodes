name = input('Whats your name?')
weight = int(input("Enter Weight in pounds:"))
height= int(input("Entre heights in inches:"))

BMI= (weight * 703)/(height * height)

print(BMI)

if BMI < 18.5:
    print(name+', You are Underweight')
elif BMI <= 24.9:
    print(name+', You are Normal weight')
elif BMI < 29.9:
    print(name+', You are Overweight')
elif BMI < 34.9:
    print(name+', You are Obese')
elif BMI < 39.9:
    print(name+', You are Severely Obese')
else:
    print(name+', You are morbidly Obese')