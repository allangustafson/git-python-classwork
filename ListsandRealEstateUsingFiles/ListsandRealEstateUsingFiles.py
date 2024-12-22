# lost half a day on this trying to figure out why my prices were so long
# read so much documentation on dictionary methods
# sudden realization at 9AM at work the next day
# I had never converted the prices to floats
# I had just been concatenating them
# I won't make that mistake again for a while lol

import csv

def getDataInput() -> list:
    '''
    Read the CSV
    All values are string format
    :return: list of lists of strings
    '''

    try:
        with open('RealEstateData.csv', 'r') as f:
            reader = csv.reader(f)
            #list of lists starting after headers
            data = [row for row in reader][1:]

    # general exception catch
    except Exception as err:
        print(f"General error: {format(err)}")

    return data

def getMedian(numbers: list) -> float:
    '''
    Calculate the median
    :param numbers: list of nums
    :return: median
    '''

    if len(numbers) % 2 != 0:
        return numbers[len(numbers) // 2]
    else:
        median1 = len(numbers) // 2
        median2 = median1 - 1
        median = (numbers[median1] + numbers[median2]) / 2
        return median

def main():
    '''
    MAIN FUNCTION
    '''

    # list of lists in string format
    lData = getDataInput()

    lPrices = []
    dCities = {}
    dZips = {}
    dTypes = {}

    # for each list in our list, referenced as a record
    for record in lData:
        # convert/validate strings from list and store in variable
        sCity = str(record[1])
        sZip = str(record[2])
        sPropertyType = str(record[7])
        fPrice = float(record[8])

        # add each price to a list of prices
        lPrices.append(fPrice)

        # <the reason I chose to write it this way>
        # if key in  dictionary increase the price value
        # else add key value pair
        if sCity in dCities:
            dCities[sCity] += fPrice
        else:
            dCities.update({sCity: fPrice})
        if sZip in dZips:
            dZips[sZip] += fPrice
        else:
            dZips.update({sZip: fPrice})
        if sPropertyType in dTypes:
            dTypes[sPropertyType] += fPrice
        else:
            dTypes.update({sPropertyType: fPrice})

    # sort for min max calcs
    lPrices.sort()
    # calculate, format, output
    print(f"{'<Summaries>':^36}")
    print(f"{'Minimum':<15} {lPrices[0]:>20,.2f}")
    print(f"{'Maximum':<15} {lPrices[-1]:>20,.2f}")
    print(f"{'Sum':<15} {sum(lPrices):>20,.2f}")
    print(f"{'Avg':<15} {sum(lPrices)/len(lPrices):>20,.2f}")
    print(f"{'Median':<15} {getMedian(lPrices):>20,.2f}")
    print()

    # dynamic output for dict items with formatting
    print(f"{'<By Property Type>':^36}")
    for k, v in dTypes.items():
        print(f"{k:<15} {v:>20,.2f}")
    print()

    print(f"{'<By City>':^36}")
    for k, v in dCities.items():
        print(f"{k:<15} {v:>20,.2f}")
    print()

    # had us store the zip so I wrote the optional output for this as well
    sAns = input("Would you like a summary by zip code as well? ")
    if sAns.lower().startswith('y'):
        print()
        print(f"{'<By Zip Code>':^36}")
        for k, v in dZips.items():
            print(f"{k:<15} {v:>20,.2f}")



main()
