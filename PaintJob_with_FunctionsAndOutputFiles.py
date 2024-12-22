
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


def getGallonsOfPaint(footage, coverage):
    '''
    calculates gallons of paint needed
    :param footage: square footage of room
    :param coverage: coverage per gallon
    :return: gallons of paint needed
    '''
    return int((footage/coverage) + 1)


def getLaborHours(hours, gallons):
    '''
    calculates hours needed
    :param hours: hours per gallon
    :param gallons: gallons needed
    :return: hours needed
    '''
    return float(hours*gallons)


def getLaborCost(hours, charge):
    '''
    calculates labor cost
    :param hours: hours needed
    :param charge: cost per hour
    :return: cost
    '''
    return float(hours*charge)


def getPaintCost(gallons, price):
    '''
    calculates paint cost
    :param gallons: gallons needed
    :param price: price per gallon
    :return: paint cost
    '''
    return float(gallons*price)


def getSalesTax(state):
    '''
    sales tax
    :param state:
    :return: tax rate
    '''
    if state in ("CT", "ct", "VT", "vt"):
        fTax = .06
    elif state in ("MA", "ma"):
        fTax = .0625
    elif state in ("ME", "me"):
        fTax = .085
    elif state in ("RI", "ri"):
        fTax = .07
    else:
        fTax = 0
    return fTax


def showCostEstimate(gallons, hours, labor_cost, paint_cost, tax_rate,):
    '''
    calculate tax and total cost
    return strings for print and file
    :param gallons: gallons needed
    :param hours: hours needed
    :param labor_cost:
    :param paint_cost:
    :param tax_rate:
    :return: string for output
    '''
    fTax = (paint_cost+labor_cost) * tax_rate
    fTotal = (float(paint_cost+labor_cost) + (fTax))
    return (
        f"Gallons of paint: {gallons:,}\n"
        f"Hours of labor: {hours:,}\n"
        f"Paint charges: ${paint_cost:,.2f}\n"
        f"Labor Charges: ${labor_cost:,.2f}\n"
        f"Tax: ${fTax:,.2f}\n"
        f"Total Cost ${fTotal:,.2f}\n"
    )


def main():
    '''
    Main Function
    '''

    # strings for input prompts
    fSquareFootage = getFloatInput("Enter wall space in square feet")
    fPaintPrice = getFloatInput("Enter paint price per gallon")
    fCoverage = getFloatInput("Enter feet per gallon")
    fGallonHours = getFloatInput("How many labor hours per gallon")
    fLaborCharge = getFloatInput("Labor Charge per hour")

    # input
    sState = str(input("(2 letter abbreviation) "
                       "State job is in: "))
    sLast = str(input("Customer Last Name: "))

    # calculate
    iTotalGallons = getGallonsOfPaint(fSquareFootage, fCoverage)
    fLaborHours = getLaborHours(fGallonHours, iTotalGallons)

    # display output
    print(showCostEstimate(iTotalGallons,
                           fLaborHours,
                           getLaborCost(fLaborHours, fLaborCharge),
                           getPaintCost(iTotalGallons, fPaintPrice),
                           getSalesTax(sState)))

    # save output to file
    outfile = open(f'{sLast}_PaintJobOutput.txt', 'w')
    outfile.write(showCostEstimate(iTotalGallons,
                                   fLaborHours,
                                   getLaborCost(fLaborHours, fLaborCharge),
                                   getPaintCost(iTotalGallons, fPaintPrice),
                                   getSalesTax(sState)))
    outfile.close()
    print(f"File: {sLast}_PaintJobOutput.txt was created.")


main()
