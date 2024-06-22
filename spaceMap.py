#!/usr/bin/python3

from tables import *
from possibleWorlds import *

import datetime
import math
import os
import random
import sys
import yaml

# an array of letters
letters = list(map(chr, range(97, 123)))
  
clear = lambda: os.system('clear')
yesses = ['Yes','yes','Y','y','Ye','ye','ya','Ya','Yup','yup']

def printMap(world, parsecs):
  #world = worldDetailed(world)
  worldArray = []
  worldCount = 10
  systemHexLocations, nearbyWorlds = nearbyPlanetsCoords(world, parsecs)
  zeroSystem = world['WorldName']
  zeroPlane = systemHexLocations[zeroSystem]
  zeroX = int(str(zeroPlane)[:2])
  zeroY = int(str(zeroPlane)[2:])
  nearbySystems = {}

  systemCount = 0
  for system in systemHexLocations:
    # traveller map's hex coordinates
    coords = systemHexLocations[system]
    # adding parsecs after zeroing in on system, shifts center right and up
    if system == zeroSystem:
      x = 0 + parsecs + 1 
      y = 0 + parsecs 
    else:
      xPos = int(str(coords)[:2]) + 1
      yPos = int(str(coords)[2:]) 
      # traveller map increases X hex position goin RIGHTWARD
      x = xPos - zeroX + parsecs
      # traveller map increases Y hex position going DOWNWARD
      y = zeroY - yPos + parsecs
    nearbySystems.update({system : { 'X' : x, 'Y' : y, 'hex' : coords }})
    systemCount += 1
    # dont add more systems than there are letters
    if systemCount >= 25:
      break

  # set height and width of map, must be larger than parsec value in all directions
  width = 2 * parsecs + 1
  height = 2 * parsecs + 1
  yCount = height
  totalSystemCount = 0

  # first create letter assignments, before printing
  for row in range(height):
    for column in range(width):
      # check if the system coordinates match the current X Y position
      for system in nearbySystems:
        x = nearbySystems[system]['X']
        y = nearbySystems[system]['Y']
        coords = nearbySystems[system]['hex']
        # y is counting down from the hieght but columns increase and start at 0, so add 1 to X
        if y == yCount and x == column + 1 : 
          letter = letters[totalSystemCount]
          nearbySystems.update({system : { 'X' : x, 'Y' : y, 'hex' : coords, 'letter' : letter }})
          totalSystemCount += 1
    yCount -= 1

  letterSystemArray = []
  for system in nearbySystems:
    letteredString = nearbySystems[system]['letter'] + ' - ' + system
    letterSystemArray.append(letteredString) 

  systemCount = len(letterSystemArray)
  systemColumns = int(systemCount / height) + (systemCount % height > 0)
  mapKey = []
  printedRow = 0
  for column in range(systemColumns):
    if column == 0:
      for row in range(height):
        pos = row
        mapKeyString = ' | ' + letterSystemArray[pos] 
        mapKey.append(mapKeyString)
    elif column >= 1:
      for row in range(height):
        pos = row + (height * column)
        try:
          letterSystemArray[pos]
          if len(mapKey[row]) < 12:
            tab = '\t\t'
          else:
            tab = '\t'
          mapKeyString = mapKey[row] + tab + ' | ' + letterSystemArray[pos] 
          mapKey[row] = mapKeyString
        except:
          mapKeyString = mapKey[row] + tab + ' | ' 
          mapKey[row] = mapKeyString
    
  possibleDots = [ '   ','   ','   ', '.  ',' . ','  .' ]
  yCount = height
  rowStrings = []
  for row in range(height):
    rowString = ''
    # ensure proper spacing on the left side of the screen
    if yCount > 9:
      bookend = ' '
    else:
      bookend = '  '
    rowString = rowString + str(yCount) + bookend
    for column in range(width):
      coordinateString = possibleDots[diceRoll(1,6) - 1]
      for system in nearbySystems:
        letter = nearbySystems[system]['letter']
        x = nearbySystems[system]['X']
        y = nearbySystems[system]['Y']
        if y == yCount and x == column + 1 : 
          coordinateString = ' ' + letter + ' '
      rowString = rowString + coordinateString
    rowString = rowString + mapKey[row]
    rowStrings.append(rowString) 
    yCount -= 1
 
  for row in rowStrings:
    print(row)

  # print out bottom row of numbers
  print('\n   ',end='')
  xCount = 1
  for column in range(width):
    if column < 9:
      print(' ',str(xCount),' ',sep='',end='')
    else:
      print(' ',str(xCount),sep='',end='')
    xCount += 1
  print()
    
def diceRoll(dieCount,dieSides):
  dieTotal = 0
  for i in range(0,dieCount):
    min = 1
    max = dieSides
    dieVal = random.randint(min,max)
    dieTotal += dieVal
  return(dieTotal)
