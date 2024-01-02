#!/usr/bin/python3

from tables import *
from possibleWorlds import *

import random
import sys

## mgt2e refers to mongoose traveller second edition 2022 update
## SWN refers to Stars Without Number free edition, which contains tons of useful tables

npcTypes = [ 'patron', 'ally', 'enemy', 'none']

npcType = sys.argv[1]
age = sys.argv[2]
try:
  npcCount = int(sys.argv[3])
except:
  pass


def main(npcType = 'any', age = 'any', npcCount = 1):
  for i in range(npcCount):
    # job from 'patron' or 'allies and enemies' tables
    npcJob = npcJobSelect(npcType)
    # random names from donjon.bin.sh lists
    forename, surname = npcNameSelect()
    # age variations, 3 categories
    ageNum = determineAge(age) 
    # body and height 2d6 tables
    body = bodyTypes[diceRoll(2,6)] 
    height = heights[diceRoll(2,6)]
    # hair 
    hairColor = determineHair(ageNum)
    eyeColor = random.choice(eyeColors)
    # quirks
    chanceforQuirk = diceRoll(1,6) 
    if chanceforQuirk == 1:
      quirk = random.choice(characterQuirks)
    else:
      quirk = ""
    npcObject = npc(npcJob, forename, surname, ageNum, body, height, hairColor, eyeColor, quirk)
    print(npcObject)

class npc:
  def __init__(self, job, forename, surname, age, body, height, hairColor, eyeColor, quirk):
    self.job = job
    self.forename= forename
    self.surname = surname
    self.fullName = str(forename + ' ' + surname)
    self.age = age
    self.body = body 
    self.height = height
    self.hairColor = hairColor 
    self.eyeColor = eyeColor 
    self.quirk = quirk

  def __str__(self):
    return f"""
           {self.job} - {self.fullName} - {self.quirk}
           {self.age} - {self.body} and {self.height}
           hair: {self.hairColor}
           eyes: {self.eyeColor}
           """

def npcJobSelect(npcType):
  if npcType not in npcTypes and npcType != 'any':
    print(npcType,'is not a valid npc type')
    print('choose from',npcTypes)
    quit()
  if npcType == 'any':
    npcType = random.choice(['ally','patron'])

  if npcType == 'ally' or 'enemy':
    npcTable = alliesEnemies
  if npcType == 'patron':
    npcTable = patrons
  if npcType == 'none':
    return ' '

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
    age = random.choice(['young','young','middle-aged','middle-aged','old'])
  npcAges = { 
    'young' : random.randint(18,29),
    'middle-aged' : random.randint(30,50),
    'old' : random.randint(51,80)
  }
  ageNum = npcAges[age] 
  return ageNum

def determineHair(age):
  grayChance = 0
  if age > 35:
    grayChance = age + diceRoll(3,8)

  naturalHairChance = diceRoll(1,6)
  if naturalHairChance <= 2:
    hairList = unnaturalHairColors 
  hairList = naturalHairColors
  hairRoll = int(diceRoll(1,len(hairList)) - 1)
  hairColor= sorted(hairList)[hairRoll]

  # if natural hair, chance of gray hair
  if hairList == naturalHairColors and hairColor not in ('dark gray','gray','silver','white'):
    # partial grey
    if grayChance >= 60:
      grayRoll = int(diceRoll(1,len(grayedHair)) - 1)
      grayness = sorted(grayedHair)[grayRoll]
      hairColor = hairColor + ' with ' + grayness
    # all grey
    elif grayChance >= 65:
      hairColor = 'gray'
    # all white
    elif grayChance >= 75:
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

main(npcType, age, npcCount)
