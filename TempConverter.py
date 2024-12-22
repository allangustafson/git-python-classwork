# Constants
FAHRENHEIT_BOIL = 212
CELSIUS_BOIL = 100

# Get User input
fTemp = float(input("Enter a temperature: "))
strFormat = str(input("Is the temp F for Fahrenheit or C for Celsius? "))

# Check for Valid Input
if strFormat not in ("F", "f", "C", "c"):
    print("Enter a F or C")
    raise SystemExit

# If 'F' Error if Temp > 212
# Convert Fahrenheit to Celsius and output
if strFormat in ("F", "f"):
    if fTemp > FAHRENHEIT_BOIL:
        print("Temp can not be > 212""\u00b0""F")
        raise SystemExit
    else:
        fCelsius = (5.0 / 9) * (fTemp - 32)
        print(f"The Celsius Equivalent is {fCelsius:.1f}""\u00b0""C")

# If 'C' Error if Temp > 100
# Convert Celsius to Fahrenheit and output
elif strFormat in ("C", "c"):
    if fTemp > CELSIUS_BOIL:
        print("Temp can not be > 100""\u00b0""C")
        raise SystemExit
    else:
        fFahrenheit = ((9.0 / 5.0) * fTemp) + 32
        print(f"The Fahrenheit Equivalent is {fFahrenheit:.1f}""\u00b0""F")
