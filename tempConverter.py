convertTo=input("Enter the unit you want to convert to (C or F): ").lower()

getTemp=float(input("Enter the temperature: "))

if convertTo == "C".lower():
    convertedTemp = (getTemp - 32) * 5/9
    print(f"The temperature in Celsius is: {convertedTemp}")
elif convertTo == "F".lower():
    convertedTemp = getTemp * 9/5 + 32
    print(f"The temperature in Fahrenheit is: {convertedTemp}")
else:
    print("Invalid unit. Please enter either 'C' or 'F'.")
