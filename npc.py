#!/usr/bin/python3

from tables import *
from possibleWorlds import *

import random
import sys

## mgt2e refers to mongoose traveller second edition 2022 update
## SWN refers to Stars Without Number free edition, which contains tons of useful tables

npcTypes = [ 'patron', 'ally', 'enemy']
npcAges = { 'young' : random.randint(18,29),
            'middle-aged' : random.randint(30,50),
            'old' : random.randint(51,80)
          }

npcType = sys.argv[1]
age = sys.argv[2]

def main(npcType = 'any', age = 'any'):
  # job from 'patron' or 'allies and enemies' tables
  npcJob = npcJobSelect(npcType)
  # random names from donjon.bin.sh lists
  forename, surname = npcNameSelect()
  # age variations, 3 categories
  age = determineAge(age) 
  # hair 
  hairColor = determineHair(age)
  npcObject = npc(npcJob, forename, surname, age, hairColor)
  print(npcObject)

class npc:
  def __init__(self, job, forename, surname, age, hairColor):
    self.job = job
    self.forename= forename
    self.surname = surname
    self.fullName = str(forename + ' ' + surname)
    self.age = age
    self.hairColor = hairColor 

  def __str__(self):
    return f"{self.job} - {self.fullName} - {self.age} - {self.hairColor}"

def npcJobSelect(npcType):
  if npcType not in npcTypes and npcType != 'any':
    print(npcType,'is not a valid npc type')
    print('choose from',npcTypes)
    quit()
  if npcType == 'any':
    npcType = random.choice(['ally','patron'])

  if npcType == 'ally' or 'enemy':
    npcTable = alliesEnemies
  elif npcType == 'patron':
    npcTable = patrons

  # create npc job
  npcJobRoll = int(diceRoll(1,len(npcTable)) - 1)
  npcJob = sorted(npcTable)[npcJobRoll]
  return npcJob

def npcNameSelect():
  # masc or fem appearance
  if diceRoll(1,2) == 2:
    forelist = mascNames
  else:
    forelist = femNames
  # npc name
  forenameRoll = int(diceRoll(1,len(forelist)) - 1)
  forename = sorted(forelist)[forenameRoll]
  surnameRoll = int(diceRoll(1,len(surnames)) - 1)
  surname = sorted(surnames)[surnameRoll]
  return forename, surname

def determineAge(age):
  if age == 'any':
    ageNum = random.randint(18,80)
  else:
    ageNum = npcAges[age] 
  return ageNum

def determineHair(age):
  if age > 35:
    greyChance = age + diceRoll(3,8)
  naturalHairChance = diceRoll(1,6)
  if naturalHairChance <= 2:
    hairList = unnaturalHairColors 
  else:
    hairList = naturalHairColors
  hairRoll = int(diceRoll(1,len(hairList)) - 1)
  hairColor= sorted(hairList)[hairRoll]

  # partial grey
  if greyChance >= 65:
    grayRoll = int(diceRoll(1,len(grayedHair)) - 1)
    grayness = sorted(grayedHair)[grayRoll]
    hairColor = hairColor + ' with ' + grayness
  # all grey
  elif greyChance >= 70:
    hairColor = 'gray'
  # all white
  elif greyChance >= 80:
    hairColor = random.choice('silver','white')

  return hairColor


def diceRoll(dieCount,dieSides):
  dieTotal = 0
  for i in range(0,dieCount):
    min = 1
    max = dieSides
    dieVal = random.randint(min,max)
    dieTotal += dieVal
  return(dieTotal)

main(npcType, age)
