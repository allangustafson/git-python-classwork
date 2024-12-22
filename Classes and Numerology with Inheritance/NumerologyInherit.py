from NumerologyLifePathDetails import ClientPath, Test


def main():
    """
    MAIN FUNCTION
    """
    sName = ""
    sDOB = ""

    #If test method fails. Will ask for valid input and try again
    while not sName:
        sName = Test.nameTest(input("Test Name: "))
    while not sDOB:
        sDOB = Test.dateTest(input("Test DOB: "))

    #Instantiates a Client object
    myClient = ClientPath(sName, sDOB)

    print(myClient)


if __name__ == "__main__":
    main()
