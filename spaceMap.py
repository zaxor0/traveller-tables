#!/usr/bin/python3

from mechanics import *
from tables import *
from possibleWorlds import *

import datetime
import getch
import math
import os
import sys
import yaml

def printMap(world, sector, parsecs, jumpRange):
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
        # this is the letter + the system name
        length = len(letterSystemArray[pos])
        if length > 13:
          tab = '   '
        elif length < 12:
          tab = '\t' 
        elif length < 8:
          tab = '\t\t' 
        mapKeyString = ' | ' + letterSystemArray[pos] + tab 
        mapKey.append(mapKeyString)
    elif column >= 1:
      for row in range(height):
        pos = row + (height * column)
        try:
          letterSystemArray[pos]
          if len(letterSystemArray[pos]) > 12:
            tab = '\t'
          else:
            tab = '\t\t'
          mapKeyString = mapKey[row] + ' | ' + letterSystemArray[pos] + tab 
          mapKey[row] = mapKeyString
        except:
          mapKeyString = mapKey[row] + ' | ' 
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
  
  possibleJumps(world, jumpRange, letterSystemArray)
  printWorldDetails(nearbySystems, sector)

def possibleJumps(world, jumpRange, letterSystemArray):
  reachableSystems = jumpSearch(world,jumpRange)
  currentWorld = ''
  reachableWorlds = ''
  for letteredSystem in letterSystemArray:
    letter = letteredSystem.split(' - ')[0]
    lSystem = letteredSystem.split(' - ')[1]
    for rSystem in reachableSystems['Worlds']:
      if rSystem['Name'] == lSystem and rSystem['Name'] == world['WorldName']:
        currentWorld = letteredSystem
      elif rSystem['Name'] == lSystem and rSystem['Name'] != world['WorldName']:
        reachableWorlds = reachableWorlds + letteredSystem + '    '
  print('# You are in: ',currentWorld,' and you can jump to: ')
  print(' ',reachableWorlds,'\n')
    
def printWorldDetails(nearbySystems,sector):
  print('Select a world (letter) for more info, or ESC to return to previous menu')
  playerKey = getch.getch()
  if playerKey != chr(27): # quit
    selectedWorld = playerKey
    for system in nearbySystems:
      if selectedWorld == nearbySystems[system]['letter']:
        world = worldSearch(system, sector)
        world = worldDetailed(world)
    print('Sector:',world['SectorName'],'Sub Sector:',world['SubsectorName'])
    print('World:',world['WorldName'],'\tUWP:',world['WorldUwp'])
    print('Remarks:',world['WorldRemarks'])
    uwp = uwpTranslator(world['WorldUwp'])
    for feature in uwp:
      print(feature,'-',uwp[feature])
    input('press Enter to continue')
