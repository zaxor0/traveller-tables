#!/usr/bin/python3

from spaceMap import *
from tables import *
from possibleWorlds import *

import datetime
import math
import os
import random
import sys
import yaml

## mgt2e refers to mongoose traveller second edition 2022 update
## SWN refers to Stars Without Number free edition, which contains tons of useful tables

shipFile = sys.argv[1]
worldName = sys.argv[2]
sectorName = False
try:
  sectorName = str(sys.argv[3])
except:
  pass

clear = lambda: os.system('clear')

yesses = ['Yes','yes','Y','y','Ye','ye','ya','Ya','Yup','yup']
nos    = ['No','no','N','n','Nope','nope','Nah','nah']
ship = {}

def main(): 
  clear()
  loadShipFile(shipFile)
  currentSystem = systemDetails(worldName) 
  currentSystemName = currentSystem['WorldName']
  printMap(currentSystem, 5)

def loadShipFile(shipFile):
  # your ship details
  with open(shipFile, 'r') as file:
    ship = yaml.safe_load(file)

def systemDetails(worldName):
  if sectorName:
    world = worldSearch(worldName, sectorName)
  else:
    world = worldSearch(worldName)
  currentSystem = worldDetailed(world)
  return currentSystem

main()
