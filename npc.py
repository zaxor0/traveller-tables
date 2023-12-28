#!/usr/bin/python3

from tables import *
from possibleWorlds import *

import random
import sys

## mgt2e refers to mongoose traveller second edition 2022 update
## SWN refers to Stars Without Number free edition, which contains tons of useful tables

npcType = sys.argv[1]
age = sys.argv[2]

npcTypes = [ 'any', 'patron', 'ally', 'enemy']

def main(npcType = 'any', age = 'middle-aged'):
  if npcType not in npcTypes:
    print(npcType,'is not a valid npc type')
    print('choose from',npcTypes)
    quit()
  elif npcType == 'ally' or 'enemy':
    npcTable = alliesEnemies
  elif npcType == 'patron':
    npcTable = patrons
  # masc or fem appearance
  if diceRoll(1,2) == 2:
    forelist = mascNames
  else:
    forelist = femNames
  # create npc job
  npcTypeRoll = int(diceRoll(1,len(npcTable)) - 1)
  npcAbc = sorted(npcTable)[npcTypeRoll]

  # npc name
  forenameRoll = int(diceRoll(1,len(forelist)) - 1)
  forename = sorted(forelist)[forenameRoll]
  surnameRoll = int(diceRoll(1,len(surnames)) - 1)
  surname = sorted(surnames)[surnameRoll]

  # age variations
  if age == 'young':
    age = int(16 + diceRoll(2,6))
  if age == 'middle-aged':
    age = int(25 + diceRoll(5,6))
  if age == 'old':
    age = int(45 + diceRoll(5,6))

  # hair 
  if age > 30:
    greyChance = age + diceRoll(2,20)

  naturalHairChance = diceRoll(1,6)
  if naturalHairChance <= 2:
    hairList = unnaturalHairColors 
  else:
    hairList = naturalHairColors
  hairRoll = int(diceRoll(1,len(hairList)) - 1)
  hairColor= sorted(hairList)[hairRoll]


  npcDef = str(npcAbc + ' - ' + forename + ' ' + surname + ' age ' + str(age))
  print(npcDef, hairColor)

class npc:
  def __init__(self, patron, mission):
    self.patron = patron
    self.mission = mission

def diceRoll(dieCount,dieSides):
  dieTotal = 0
  for i in range(0,dieCount):
    min = 1
    max = dieSides
    dieVal = random.randint(min,max)
    dieTotal += dieVal
  return(dieTotal)


main(npcType, age)
