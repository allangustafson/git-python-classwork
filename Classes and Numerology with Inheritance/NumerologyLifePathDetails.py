"""
NUMEROLOGY MODULE with INHERITANCE
For testing and calculating Numerology
"""
from re import match


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

    @property
    def Name(self) -> str:
        """
        :return: Name
        """
        return self.__basename

    @property
    def Birthdate(self) -> str:
        """
        :return: Date of Birth
        """
        return self.__basedob

    @property
    def Attitude(self) -> str:
        """
        :return: Attitude Number
        """
        return self.__reduce(self.__dob[0] + self.__dob[1] +
                             self.__dob[2] + self.__dob[3])

    @property
    def BirthDay(self) -> str:
        """
        :return: Birthday Number
        """
        return self.__reduce(self.__dob[2] + self.__dob[3])

    @property
    def LifePath(self) -> str:
        """
        :return: Life Path Number
        """
        return self.__reduce(self.__dob)

    @property
    def Personality(self) -> str:
        """
        :return: Personality Number
        """
        return self.__reduce(self.__consonantnum)

    @property
    def PowerName(self) -> str:
        """
        :return: Power Name Number
        """
        return self.__reduce(self.Personality + self.Soul)

    @property
    def Soul(self) -> str:
        """
        :return: Soul Number
        """
        return self.__reduce(self.__vowelnum)


    def __str__(self):
        """
        Return string if client object is called
        :return: Numerology Summary
        """
        return (f"\n{'Client Name: ':15}{self.Name}"
                f"\n{'Client DOB: ':15}{self.Birthdate}"
                f"\n{'Life Path: ':15}{self.LifePath}"
                f"\n{'Attitude: ':15}{self.Attitude}"
                f"\n{'Birthday: ':15}{self.BirthDay}"
                f"\n{'Personality: ':15}{self.Personality}"
                f"\n{'Power Name: ':15}{self.PowerName}"
                f"\n{'Soul: ':15}{self.Soul}")




class ClientPath(Client):
    '''
    CLIENTPATH CLASS
    subclass of Client
    adds Life Path Description
    '''


    def __init__(self, name: str, dob: str):
        """
        Create a clientpath object
        """

        super().__init__(name, dob)
        match self.LifePath:
            case "1":
                self.__Descriptor = "The Independent: Wants to work/think for themselves"
            case "2":
                self.__Descriptor = "The Mediator: Avoids conflict and wants love and harmony"
            case "3":
                self.__Descriptor = "The Performer: Likes music, art and to perform or get attention"
            case "4":
                self.__Descriptor = "The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful"
            case "5":
                self.__Descriptor = "The Adventurer: Likes to travel and meet others, often an extrovert"
            case "6":
                self.__Descriptor = "The Inner Child: Is meant to be a parent and/or one that is young at heart"
            case "7":
                self.__Descriptor = "The Naturalist: Enjoy nature and water and alternative life paths, open to spirituality"
            case "8":
                self.__Descriptor = "The Executive: Gravitates to money and power"
            case "9":
                self.__Descriptor = "The Humanitarian: Helps others and/or experiences pain and learns the hard way"


    @property
    def LifePathDescription(self) -> str:

        return self.__Descriptor


    def __str__(self):
        """
        Return string if client object is called
        :return: Numerology Summary with Life Path Description
        """
        return (f"\n{'Client Name: ':15}{self.Name}"
                f"\n{'Client DOB: ':15}{self.Birthdate}"
                f"\n{'Life Path: ':15}{self.LifePath}"
                f"\n{'Attitude: ':15}{self.Attitude}"
                f"\n{'Birthday: ':15}{self.BirthDay}"
                f"\n{'Personality: ':15}{self.Personality}"
                f"\n{'Power Name: ':15}{self.PowerName}"
                f"\n{'Soul: ':15}{self.Soul}"
                f"\n{self.LifePathDescription}")




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


