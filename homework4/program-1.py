# Write a function that converts temperature from Fahrenheit to Celsius using formula
def temperature_convertion(temperature_value):
    temperature_celsius=(5/9)*(temperature_value-32) 
    return round(temperature_celsius,2)

temperature_value=float(input("Enter temperature in Fahrenheit : "))
temperature_celsius=temperature_convertion(temperature_value)
print("Temperatue in Celsius : ",temperature_celsius)
