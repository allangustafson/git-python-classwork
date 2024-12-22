
# Constants for Surface Gravity Factors
nMERCURY_GF = 0.38
nVENUS_GF = 0.91
nMOON_GF = 0.165
nMARS_GF = 0.38
nJUPITER_GF = 2.34
nSATURN_GF = 0.93
nURANUS_GF = 0.92
nNEPTUNE_GF = 1.12
nPLUTO_GF = 0.066

# Gets name and Earth weight of user
# Formats weight as float
sName = input("What is your name: ")
nEarthWeight = float(input("What is your weight: "))

#I could have done calculations here and stored them in a variable
#I chose to do them in the f-strings as they won't be needed elsewhere in this program

# Calculates and display planetary weights
# Text formatted to 20 spaces to keep everything in line
# Weights formatted to 10 spaces and accurate to 2 decimal places
print(f"{sName} here are your weights on our Solar System's planets:")
print(f"{"Weight on Mercury:":20}{nEarthWeight*nMERCURY_GF:10.2f}")
print(f"{"Weight on Venus:":20}{nEarthWeight*nVENUS_GF:10.2f}")
print(f"{"Weight on our Moon:":20}{nEarthWeight*nMOON_GF:10.2f}")
print(f"{"Weight on Mars:":20}{nEarthWeight*nMARS_GF:10.2f}")
print(f"{"Weight on Jupiter:":20}{nEarthWeight*nJUPITER_GF:10.2f}")
print(f"{"Weight on Saturn:":20}{nEarthWeight*nSATURN_GF:10.2f}")
print(f"{"Weight on Uranus:":20}{nEarthWeight*nURANUS_GF:10.2f}")
print(f"{"Weight on Neptune:":20}{nEarthWeight*nNEPTUNE_GF:10.2f}")
print(f"{"Weight on Pluto:":20}{nEarthWeight*nPLUTO_GF:10.2f}")
