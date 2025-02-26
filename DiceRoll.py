#DiceRoll.py
#Name:
#Date:
#Assignment:
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  numRolls = 10000000
  for count in range (numRolls):
    dice1 = random.randiant(1,6)
    dice2 = random.randiant(1,6)
    total = dice1 + dice2

    rolls(total) = [total] + 1
    #print(dice1. dice2, total)
  #find the sum total of the two dice
  
  #print statictics for dice rolls
  print(rolls)
  num = 2
  for r in rolls:
    perecent = round(r / numRolls * 100, 1)
    print(num , ":", r, perecent)
    num = num + 1




if __name__ == '__main__':
  main()
