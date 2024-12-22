# functions for paintjob calculations
import math


def pos_number(prompt, minValue=1, errors=True) -> float:
    """Reprompts until a float above the minimum is given.\n
    errors = (Prints error message)
    """
    amount = minValue - 1
    while amount < minValue:
        try:
            amount = float(input(prompt))
            if amount < minValue:
                print(f"Must be a greater than {minValue-1}") if errors else None

        except KeyboardInterrupt:
            raise SystemExit
        except:
            print("Must be numeric") if errors else None

    return amount


def getGallonsOfPaint(squareFeet, feetPerGal) -> int:
    """Returns the number of gallons required based on square feet"""
    return math.ceil(squareFeet / feetPerGal)


def getLaborHours(laborGallon, gallonsOf) -> float:
    """Returns labor hours based on labor per gallon and the amount of gallons of paint."""
    return laborGallon * gallonsOf


def getLaborCost(laborGallon, laborPerHour) -> float:
    return laborGallon * laborPerHour


def getPaintCost(gallons, pricePerGallon) -> float:
    return gallons * pricePerGallon


def getSalesTax(key) -> float:
    """Returns the sales tax for the Northeast states.
    If the state is not present, returns national average sales tax of 7%
    """

    dctTax = {"CT": 0.06, "MA": 0.0625, "ME": 0.085, "NH": 0.0, "RI": 0.07, "VT": 0.06}

    fTax = dctTax.get(key.upper())
    if fTax == None:
        return 0.07  # Returns the average sales tax for the US
    else:
        return fTax


def showCostEstimate(paint, labor, tax) -> str:
    fTotalCost = paint + labor + tax
    return f"The total cost of services: {'{:,.2f}'.format(fTotalCost)}"


def format_dollar(num) -> str:
    """Returns dollar amount formatted string.\n
    '$x,xxx.xx'
    """
    return f"${ '{:,.2f}'.format(num) }"


sTitle = """
___  ____ _ _  _ ___    
|__] |__| | |\ |  |     
|    |  | | | \|  |     
                        
____ _  _ ____ ___ ____ 
|  | |  | |  |  |  |___ 
|_\| |__| |__|  |  |___ 


"""
