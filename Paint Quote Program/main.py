from functions import *


def main():

    # Lots of variables
    fSquareFeet = pos_number(("Enter wall space in square feet: "))
    fPriceGallon = pos_number("Enter price per gallon: ")
    fFeetPerGallon = pos_number("Enter feet per gallon: ")
    fHoursPer = pos_number("How many hours per gallon: ")
    fLaborHourly = pos_number("Labor charge per hour: ")
    fStateJob = getSalesTax(input("State job is in: "))
    sLastName = input("Enter customer's last name: ")

    iGallons = getGallonsOfPaint(fSquareFeet, fFeetPerGallon)
    fLaborAmount = getLaborHours(fHoursPer, iGallons)
    fPaintCost = getPaintCost(iGallons, fPriceGallon)
    fLaborCost = getLaborCost(fHoursPer, fLaborHourly) * iGallons
    fSalesTax = (fLaborCost + fPaintCost) * fStateJob
    sTotalCost = showCostEstimate(fPaintCost, fLaborCost, fSalesTax)

    lstOutput = (
        f"\nThe amount of gallons needed   : {iGallons}",
        f"The amount of labor required   : {fLaborAmount}",
        f"The cost of paint              : {format_dollar(fPaintCost)}",
        f"The cost of labor              : {format_dollar(fLaborCost)}",
        f"Tax                            : {format_dollar(fSalesTax)}",
    )

    print(sTotalCost)

    for iteration in lstOutput:
        print(iteration)

    customWrite = lambda name: open(f"{name}_PaintJobOutput.txt", "w")

    with customWrite(sLastName) as nameFile:

        nameFile.write(sTitle)

        for iteration in lstOutput:
            nameFile.write(iteration + "\n")

        nameFile.write(sTotalCost)

    print("File write success")


if __name__ == "__main__":
    main()
