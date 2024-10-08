
def lab3Question1(number, cutoff):
    # Take in two arguments - a number and a 'cutoff' (another number)
    # Return True if the number is less than the cutoff, False otherwise
    # Also, print a statement of "[Number] is less than [cutoff]" or "[Number] is not less than [cutoff]"
    # Where the [Number] and [cutoff] are the actual numbers passed in
   if number < cutoff:
        print(f" {number} is less than {cutoff}")
        return True
   else:
        print(f"{number} is not less than {cutoff}")
        return False

def lab3Question2(decimal_number):
    # Take in an argument of a float (decimal) number.
    # Return "zero" if the number is 0, "positive" if the number is positive, and "negative" if the number is negative
    # Return "invalid" if the input is not a float
    if isinstance(decimal_number,(float,int)):
        if decimal_number == 0:
            return "zero"
        elif decimal_number > 0:
            return "positive"
        elif decimal_number < 0:
            return "negative"
    else:
        return "invalid"

def lab3Question3(year):
    # Take in a number that represents a year
    # Return "21st century" if the year is between 2001 and 2100,
    # "20th century" if the year is between 1901 and 2000,
    # "19th century" if the year is between 1801 and 1900, 
    # "ancient" if the year is older
    # "invalid" if the input is not an acceptable year number. 
    if not isinstance(year, int):
        return "invalid"
    elif 2001 <= year <= 2100:
        return "21st century"
    elif 1901 <= year <= 2000:
        return "20th century"
    elif 1801 <= year <= 1900:
        return "19th century"
    elif year < 1801:
        return "ancient"

def lab3Question4(number_1, number_2, number_3):
    # Take in three numbers as arguments
    # Return the largest of the three numbers
    # Return None if the inputs are not 3 numbers
    if not isinstance(number_1,(int,float)) or not isinstance(number_2, (int,float)) or not isinstance(number_3,(int,float)):
        return None
    elif number_1 > number_2 and number_1 > number_3:
        largest_number = number_1
    elif number_2 > number_1 and number_2 > number_3:
        largest_number = number_2
    else: 
        largest_number = number_3
    return largest_number

def lab3Question5(temperature, scale_used):
    # Take in a temperature and the scale that the temperature is in - either "C" for Celsius or "F" for Fahrenheit (capitalized)
    # Return "Liquid" if water is in liquid state at that temperature
    # Return "Solid" if water is in solid state at that temperature
    # Return "Gas" if water is in gas state at that temperature
    # Return "Invalid" if the temperature or scale are invalid
    #divide into farenheit and celcius
    #At low temperatures (below 0 C or below 32 F), water is a solid.
    #When at "normal" temperatures (between 0 C and 100 C/ between 32 F and 212 F), it is a liquid. 
    #At temperatures above 100 C/above 212 F, water is a gas (steam).
    #absolute zero is the lowest temperature possible 
    #at highest temperature possible (Plancks temp) water would not even be what we know water to be so we will not consider that
    absolute_zero_celcius = -273.15 
    absolute_zero_farenheit = -460
    if scale_used not in ["C","F"]:
      return "Invalid"
    if scale_used == "C":
        if temperature < absolute_zero_celcius: 
            return "Invalid"
        elif temperature < 0:
            return "Solid"
        elif 0 <= temperature < 100:
            return "Liquid"
        elif temperature > 100:
            return "Gas"
    elif scale_used == "F":
        if temperature < absolute_zero_farenheit:
            return "Invalid"
        elif temperature < 32:
            return "Solid"
        elif 32 <= temperature <= 213:
            return "Liquid"
        elif temperature > 212:
            return "Gas"
        

      


      

 