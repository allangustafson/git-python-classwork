"""
NUMEROLOGY MODULE
For testing and calculating Numerology
"""


class Client:
    """
    CLIENT CLASS
    Note that all parameters are strings
    Some possible decorator such as __reduce in the future
    Some methods could be made static. I need to learn more about this.
    """


    def __init__(self, name: str, dob: str):
        """
        Create a client object
        """
        self.__basename = name
        self.__basedob = dob
        self.__name = name.upper()
        self.__dob = dob.replace("-","").replace("/","")
        self.__vowel, self.__consonant = self.__splitVowel(self.__name)
        self.__vowelnum = self.__convertAlpha(self.__vowel)
        self.__consonantnum = self.__convertAlpha(self.__consonant)

    def __reduce(self, num: str) -> str:
        """
        Add the digits of string of numbers
        Will repeat on result until only 1 digit in result
        :return: single digit string
        """
        while len(num) > 1:
            sum_ = 0
            for digit in num:
                sum_ += int(digit)
            num = str(sum_)
        return num


    def __splitVowel(self, name: str) -> tuple[str, str]:
        """
        Separates the vowels and consonants of a string
        :return: vowel and consonant strings as tuple
        """
        lVowel = []
        lConsonant = []

        for c in name:
            if not c.isalpha():
                continue
            elif c in ["A","E", "I","O","U"]:
                lVowel.append(c)
            else:
                lConsonant.append(c)
        return "".join(lVowel), "".join(lConsonant)

    def __convertAlpha(self, name: str) -> str:
        """
        Convert string of letters into numerology numbers
        Note - No math. This method concatenates.
        :return:
        """

        sNewname = ""
        for c in name:
            match c:
                case "A" | "J" | "S":
                    sNewname += "1"
                case "B" | "K" | "T":
                    sNewname += "2"
                case "C" | "L" | "U":
                    sNewname += "3"
                case "D" | "M" | "V":
                    sNewname += "4"
                case "E" | "N" | "W":
                    sNewname += "5"
                case "F" | "O" | "X":
                    sNewname += "6"
                case "G" | "P" | "Y":
                    sNewname += "7"
                case "H" | "Q" | "Z":
                    sNewname += "8"
                case "I" | "R":
                    sNewname += "9"
        return sNewname


    def getName(self) -> str:
        """
        :return: Name
        """
        return self.__basename


    def getBirthdate(self) -> str:
        """
        :return: Date of Birth
        """
        return self.__basedob


    def getAttitude(self) -> str:
        """
        :return: Attitude Number
        """
        return self.__reduce(self.__dob[0] + self.__dob[1] +
                             self.__dob[2] + self.__dob[3])


    def getBirthDay(self) -> str:
        """
        :return: Birthday Number
        """
        return self.__reduce(self.__dob[2] + self.__dob[3])


    def getLifePath(self) -> str:
        """
        :return: Life Path Number
        """
        return self.__reduce(self.__dob)


    def getPersonality(self) -> str:
        """
        :return: Personality Number
        """
        return self.__reduce(self.__consonantnum)


    def getPowerName(self) -> str:
        """
        :return: Power Name Number
        """
        return self.__reduce(self.getPersonality() + self.getSoul())


    def getSoul(self) -> str:
        """
        :return: Soul Number
        """
        return self.__reduce(self.__vowelnum)


    def __str__(self):
        """
        Return string if client object is called
        :return: Numerology Summary
        """
        return (f"\n{'Client Name: ':15}{self.getName()}"
                f"\n{'Client DOB: ':15}{self.getBirthdate()}"
                f"\n{'Life Path: ':15}{self.getLifePath()}"
                f"\n{'Attitude: ':15}{self.getAttitude()}"
                f"\n{'Birthday: ':15}{self.getBirthDay()}"
                f"\n{'Personality: ':15}{self.getPersonality()}"
                f"\n{'Power Name: ':15}{self.getPowerName()}"
                f"\n{'Soul: ':15}{self.getSoul()}")




class Test:
    """
    TEST CLASS
    Collection of methods for numerology data validation
    """


    def nameTest(name: str) -> str:
        """
        Test that string is not empty
        :return: name or empty string
        """
        if name == "":
            print("please enter a name")
            return ""
        else:
            return name


    def dateTest(dob: str) -> str:
        """
        Test for proper date format
        :return: date or empty string
        """
        if (len(dob) == 10 and
                dob[2] in ['-', '/'] and
                dob[5] in ['-', '/']):
            return dob
        else:
            print("please use mm-dd-yyyy format")
            return ""


