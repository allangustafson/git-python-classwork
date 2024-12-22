# Get input
iYear = int(input("Enter the year: "))

# Check if evenly divisible by 4 and NOT by 100
# Check if evenly divisible by 400
# Output
if (((iYear % 4 == 0) and not (iYear % 100 == 0))
        or
        (iYear % 400 == 0)):
    print('That is a leap year. February has 29 days.')
else:
    print('That is NOT a leap year. February has 28 days.')
