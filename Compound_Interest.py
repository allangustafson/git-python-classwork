# Gets input from the user and stores it in relevant variables
nPrincipal = float(input("Enter the starting principal: "))
nStatedRate = float(input("Enter the annual interest rate: "))
nCompound = int(input("How many times per year is the interest compounded? "))
nYears = float(input("For how many years will the account earn interest? "))

# Converts the interest rate percentage into a decimal
fInterestRate = float(nStatedRate/100)

# Calculates the future value based on data provided by the user
fFutureValue = nPrincipal*(1+fInterestRate/nCompound)**(nCompound*nYears)

# Displays future value for the user
print(f"At the end of {nYears} years you will have $ {fFutureValue:,.2f}")
