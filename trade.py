#!/usr/bin/python3

from spaceMap import *
from tables import *
from possibleWorlds import *

def calcTradeCodes(system, sector):
  world = worldSearch(system, sector)
  world = worldDetailed(world)
  uwp = world['WorldUwp']
  # convert from travellers "hex" codes
  uwpArray = [ uwp[0], uwp[1], uwp[2], uwp[3], uwp[4], uwp[5], uwp[6], uwp[8] ]
  hexValues = { 'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15 }
  position = 0
  for value in uwpArray:
    for lett in hexValues:
      num = hexValues[lett]
      if value == lett:
        uwpArray[position] = num
    position += 1

  starport = uwpArray[0]
  size = int(uwpArray[1])
  atmo = int(uwpArray[2])
  hydro = int(uwpArray[3])
  pop = int(uwpArray[4])
  gov = int(uwpArray[5])
  law = int(uwpArray[6])
  tech = int(uwpArray[7])

  tradeCodes = []
  if atmo in range(4,9) and hydro in range(4,8) and pop in range(5,7):
    tradeCodes.append('Ag') # Agricultural
  if size == 0 and atmo == 0 and hydro == 0:
    tradeCodes.append('As') # Asteroid
  if pop == 0 and gov == 0 and law == 0:
    tradeCodes.append('Ba') # Barren
  if atmo in range(2,9) and hydro == 0:
    tradeCodes.append('De') # Desert
  if atmo >= 10 and hydro >= 1:
    tradeCodes.append('Fl') # Fluid Oceans
  if size in range(6,8) and atmo in range(5,8) and atmo != 7 and hydro in range(5,7):
    tradeCodes.append('Ga') # Garden
  if pop >= 9:
    tradeCodes.append('Hi') # High Population
  if tech >= 12:
    tradeCodes.append('Ht') # High Tech 
  if atmo in range(0,1) and hydro >= 1:
    tradeCodes.append('Ic') # Ice-Capped 
  if atmo in [0,1,2,4,7,9,10,11,12] and pop >= 9:
    tradeCodes.append('In') # Industrial
  if pop in range(1,3):
    tradeCodes.append('Lo') # Low Population
  if pop >= 1 and tech <= 5:
    tradeCodes.append('Lt') # Low Tech
  if atmo in range(0,3) and hydro in range(0,3) and pop >=6:
    tradeCodes.append('Na') # Low Tech
  if atmo in range(2,5) and hydro in range(0,3):
    tradeCodes.append('Po') # Poor
  if atmo in range(6,8) and pop in range(6,8) and gov in range(4,9):
    tradeCodes.append('Ri') # Rich
  if atmo == 0:
    tradeCodes.append('Va') # Vacuum
  if (atmo in range(3,9) or atmo >= 13) and hydro >= 10:
    tradeCodes.append('Wa') # Waterworld
 
  return tradeCodes

# mgt2e 242 to 245
def goodsAvailable(tradeCodes, population):
  # a planet has all its trade code goods AND common goods
  # additionally, it has "random goods" equal to the worlds population good

  # all common goods are available, roll amount per the "tons" column for a given type
  # trade goods are only present if the planet has that trade code

  # for worlds with pop 3 or less, roll DM-3, if 9 or higher, DM+3

  # per the world population code (0 to 9), roll that many 2d6 to get that many d66 values
  # those values will tell you additional goods that are available
