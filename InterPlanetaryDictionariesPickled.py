import pickle


def main():
    """
    MAIN FUNCTION
    :return:
    """

# Declare dictionaries
    dictPlanetHistory = {}
    dictPersonWeights = {}
    dictConversion = {
        "Mercury" : 0.38,
        "Venus" : 0.91,
        "Moon" : 0.165,
        "Mars" : 0.38,
        "Jupiter" : 2.34,
        "Saturn" : 0.93,
        "Uranus" : 0.92,
        "Neptune" : 1.12,
        "Pluto" : 0.066
    }

# Try opening binary history file and load content as dictionary
# Pass if file not found
    eof = False
    try:
        input_file = open('agPlanetaryWeights.db', 'rb')
        while not eof:
            try:
                dictPlanetHistory = pickle.load(input_file)
            except EOFError:
                eof = True
        input_file.close()
    except FileNotFoundError:
        pass



# Choice to display the records pulled from the history file
### COULD BE A FUNCTION ###
    sHist = input("Would you like to see the history y/n: ")
    if sHist.lower() == "y":
        for k, v in dictPlanetHistory.items():
            print(
                f"{k}, here are your weights on our Solar System's planets")
            for x, y in v.items():
                print(f"Weight on {x}{":":{10-len(x)}} {y:>10.2f}")



# Get name and weight for each person
# Name must be unique
# Dynamically add new entries
# dictConversion  [planet : gravity factor]
# dictPersonWeights [name : converted weights]
# dictPlanetHistory [name : {dictPersonWeights}]
### COULD BE A FUNCTION ###
    sName = "x"
    while sName != "":
        sName = input("What is your name (enter key to quit): ")
        if sName == "": break
        if sName not in dictPlanetHistory:
            while True:
                try:
                    fWeight = float(input("What is your weight: "))
                    if fWeight <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Input a valid number")

            dictPersonWeights = {k: v * fWeight for k, v in
                                 dictConversion.items()}
            dictPlanetHistory.update({sName: dictPersonWeights})
            print(
                f"{sName}, here are your weights on our Solar System's planets")
            for k, v in dictPersonWeights.items():
                print(f"Weight on {k}{":":{10-len(k)}} {v:>10.2f}")
        else:
            print(f"{sName} is already in the history file. Enter a unique name.")


# Save the dictionary as a binary file
    output_file = open('agPlanetaryWeights.db', 'wb')
    pickle.dump(dictPlanetHistory, output_file)
    output_file.close()


main()
