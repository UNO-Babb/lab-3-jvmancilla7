#TempConvert.py
#Name:Juan Mancilla Vargas
#Date:2/3/2025
#Assignment:TempConvert


def main():
  #Prompt the user for a Fahrenheit temperature
  tempF= float(input("Enter temperature in Fahrenheit"))
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  

  tempC = (5/9)*(tempF - 32)
  tempC= round(tempC,1)


  print(tempF, "F is ",tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
