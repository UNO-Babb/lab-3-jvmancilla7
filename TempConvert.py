#TempConvert.py
#Name:Juan Mancilla Vargas
#Date:2/3/2025
#Assignment:TempConvert


def main():
  #Prompt the user for a Fahrenheit temperature
 
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF= 100

  tempC = (5/9)*(tempF - 32)
  tempC= round(tempC,2)

  print("Enter temperature in Fahrenheit",tempF)

  print(tempF, "F is ",tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
