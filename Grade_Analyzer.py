
# Declare Variables
iLow = 0
iDivisor = 4
sGrade = "Unassigned"

# Get User Input
sName = str(input("Name: "))
iTest1 = int(input("Test 1: "))
iTest2 = int(input("Test 2: "))
iTest3 = int(input("Test 3: "))
iTest4 = int(input("Test 4: "))

# Test that all scores are not less than zero
if iTest1 < 0 or iTest2 < 0 or iTest3 < 0 or iTest4 < 0:
    print("Test scores must be greater than 0")
    raise SystemExit

# Ask user if they would like to have their lowest grade dropped
else:
    sDrop = str(input("Would you like to drop Lowest Grade, Y or N? "))
# Check for Valid Input
if sDrop not in ("Y", "y", "N", "n"):
    print("Please enter a valid character")
    raise SystemExit


# Assigns the Divisor for Average Calculation and
# Determine the lowest grade if user selects yes

elif sDrop in ("Y", "y"):
    iDivisor = 3
    if iTest1 < iTest2 and iTest3 and iTest4:
        iLow = iTest1
    elif iTest2 < iTest3 and iTest4:
        iLow = iTest2
    elif iTest3 < iTest4:
        iLow = iTest3
    else:
        iLow = iTest4

# Calculate the Average
# If user selects no, iLow and iDivisor still have their default values
fAverage = (iTest1+iTest2+iTest3+iTest4-iLow) / iDivisor

# Determine Letter Grade based on Average
if fAverage >= 97:
    sGrade = "A+"
elif fAverage >= 94:
    sGrade = "A"
elif fAverage >= 90:
    sGrade = "A-"
elif fAverage >= 87:
    sGrade = "B+"
elif fAverage >= 84:
    sGrade = "B"
elif fAverage >= 80:
    sGrade = "B-"
elif fAverage >= 77:
    sGrade = "C+"
elif fAverage >= 74:
    sGrade = "C"
elif fAverage >= 70:
    sGrade = "C-"
elif fAverage >= 67:
    sGrade = "D+"
elif fAverage >= 64:
    sGrade = "D"
elif fAverage >= 60:
    sGrade = "D-"
elif fAverage < 60:
    sGrade = "F"

# Output
print(f"{sName}'s test average is: {fAverage:.1f}")
print(f"Letter Grade for this average is {sGrade}")
