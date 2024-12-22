# Variables
fDeposit = 0.0
fInterestRate = 0.0
iMonths = 0
fGoal = -1.0

# Input and Validation
while True:
    try:
        fDeposit = float(input("What is the Original Deposit "
                               "(positive value): "))
        if fDeposit <= 0:
            print("input must be a positive numeric value")
            continue
        else:
            break

    except ValueError:
        print("input must be a positive numeric value")
        continue

while True:
    try:
        fInterestRate = float(input("What is the Interest Rate "
                                    "(positive value): "))
        if fInterestRate <= 0:
            print("input must be a positive numeric value")
            continue
        else:
            break
    except ValueError:
        print("input must be a positive numeric value")
        continue

while True:
    try:
        iMonths = int(input("What is the Number of Months "
                            "(positive value): "))
        if iMonths <= 0:
            print("input must be a positive numeric value")
            continue
        else:
            break
    except ValueError:
        print("input must be a positive numeric value")
        continue

while True:
    try:
        fGoal = float(input("What is the Goal Amount "
                            "(can enter 0 but not negative): "))
        if fGoal < 0:
            print("input must be a positive numeric value")
            continue
        else:
            break
    except ValueError:
        print("input must be a positive numeric value")
        continue

# Converts the interest rate percentage into a decimal for monthly
fConvertedRate = float((fInterestRate/100) / 12.0)

# Loop Through Months and Output the Balance Progressively
fBalance = fDeposit
for i in range(1, iMonths + 1):
    fInterest = fBalance * fConvertedRate
    fBalance += fInterest
    print(f"Month: {i} Account Balance: ${fBalance:.2f}")

# Loop until Balance reaches the Goal
fBalance = fDeposit
iCounter = 0
while fBalance < fGoal:
    fInterest = fBalance * fConvertedRate
    fBalance += fInterest
    iCounter += 1
print(f"It will take: {iCounter} months to reach the goal of ${fGoal:.2f}")
