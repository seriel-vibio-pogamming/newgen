print("This program converts temperatures (°F --> °C)")
print("Press [F] to convert from Fahrenheit to Celsius")
print("Press [C] to convert from Celsius to Fahrenheit")
fc = input("Select [F/C]: ")
while fc != "F" and fc!= "C":
    fc = input("You must select between [F/C]: ")

if fc == "F":
    ftoc = int(input("Please enter degrees Fahrenheit: "))
    ftoc = (ftoc - 32) * 5/9
    print(str(ftoc) + " °C")
elif fc == "C":
    ctof = int(input("Please enter degrees Celsius: "))
    ctof = (ctof * 1.8) + 32
    print(str(ctof) + " °F")
