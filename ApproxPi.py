#ApproxPi.py
#Name: Juan V Mancilla Vargas
#Date:2/3/2025
#Assignment:ApproxPi
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  precision= int(input("How many decimal places do you want to approximate pie?"))

  start = time.time()
  #calculate pi using the approximation technique
  #Loop until the level of percision is reached
  approxPi = 4/1
  sign = -1
  denom = 3
  while round(approxPi,precision) != round(realPi,precision):
    
    approxPi= approxPi + (sign * 4 / denom)

    sign = sign * -1
    denom= denom + 2

  end = time.time()

  elapsedTime = end - start
  print(elapsedTime)

if __name__ == '__main__':
  main()
