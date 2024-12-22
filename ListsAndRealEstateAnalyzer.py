def getFloatInput(prompt):
    '''
    gets input, converts to float, validates input
    :param prompt: variable strings for input prompts
    :return: float after conversion
    '''
    while True:
        try:
            fConverted = float(input(f"{prompt}: "))
            if fConverted <= 0:
                print("input must be a positive numeric value")
                continue
            else:
                return fConverted
        except ValueError:
            print("input must be a positive numeric value")
            continue


def getMedian(numbers):
    '''
    calculates median for list
    :param numbers: list
    :return: median
    '''
    numbers.sort()
    if len(numbers) % 2 != 0:
        median = len(numbers)//2
        return numbers[median]
    else:
        median1 = len(numbers)//2
        median2 = median1 - 1
        median = (numbers[median1]+numbers[median2])/2
        return median


def main():
    '''
    MAIN FUNCTION
    '''

    # CONSTANTS and variables
    fCOMMISSION_RATE = .03
    fSales = []
    again = 'Y'

    # Get property values, add to list
    while again.upper() != 'N':
        fSales.append(getFloatInput("Enter property sales value"))
        while True:
            again = str(input("Enter another value Y or N: "))
            if again.upper() not in ['Y', 'N']:
                continue
            else:
                break
    fSales.sort()

    # Output
    count = 0
    for element in fSales:
        count += 1
        print(f"Property {count} ${element:,.2f}")
    fTotal = sum(fSales)
    print(('{: <12}'.format("Minimum: "))+f"${min(fSales):,.2f}")
    print(('{: <12}'.format("Maximum: "))+f"${max(fSales):,.2f}")
    print(('{: <12}'.format("Total: "))+f"${fTotal:,.2f}")
    print(('{: <12}'.format("Average: "))+f"${fTotal/count:,.2f}")
    print(('{: <12}'.format(f"Median: "))+f"${getMedian(fSales):,.2f}")
    print(('{: <12}'.format(f"Commission: "))+
          f"${fTotal*fCOMMISSION_RATE:,.2f}")


main()
