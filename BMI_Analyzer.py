
# Declare Constants
HEIGHTCONVERTER = 39.36
WEIGHTCONVERTER = 2.2
UNDERWEIGHT = 18.5
NORMAL = 24.9
OVERWEIGHT = 29.9

# Declare Variables
sFinding = "Unassigned"

# Intro
print("\nHello my name is Allan Gustafson "
      "and I will be calculating your BMI today!\n")
# Get User Input
sName = str(input("Your Name: "))
iHeight = int(input("Height in whole inches: "))
iWeight = int(input("Weight in whole pounds: "))

# Convert Imperial to Metric
fConvertedHeight = iHeight / HEIGHTCONVERTER
fConvertedWeight = iWeight / WEIGHTCONVERTER
fBMI = fConvertedWeight / (fConvertedHeight**2)

# Determine BMI Category
if fBMI <= UNDERWEIGHT:
    sFinding = "Underweight"
elif fBMI <= NORMAL:
    sFinding = "Normal"
elif fBMI <= OVERWEIGHT:
    sFinding = "Overweight"
elif fBMI > OVERWEIGHT:
    sFinding = "Obese"

# Output
print(f"{sName} your BMI is {fBMI:,.2f}.")
print(f"According to this calculation you are \033[1m{sFinding}\033[0m!")
