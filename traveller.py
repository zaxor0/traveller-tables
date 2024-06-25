#!/usr/bin/python3

from spaceMap import *
from tables import *
from possibleWorlds import *

import os

import datetime
import math
import random
import sys
import yaml
import getch

# variables
saveDir = 'saves/'
worldName = ""
parsecs = 5

# player input options
keys = { '1' : 'ship details', '2' : 'map view' , '3' : 'Jump' , 'ESC' : 'Quit'}

# arguments, only accept save files
try:
  saveFile = sys.argv[1]
except:
  saveFile = False 

clear = lambda: os.system('clear')


letters = list(map(chr, range(97, 123)))
yesses = ['Yes','yes','Y','y','Ye','ye','ya','Ya','Yup','yup']
nos    = ['No','no','N','n','Nope','nope','Nah','nah']
ship = {}

def main(saveFile): 
  saveFile, saveFileName = loadingScreen(saveFile)
  saveFile = loadSave(saveFile)
  gameActive = True
  while gameActive == True:
    system = saveFile['location']['system']
    sector = saveFile['location']['sector']
    ship = saveFile['ship'] 
    currentSystem = systemDetails(system,sector) 
    currentSystemName = currentSystem['WorldName']
    saveFile = playerInput(currentSystem, sector, parsecs, ship, saveFile)
    autoSave(saveFileName, saveFile)

def loadSave(saveFile):
  print('...loading',str(saveFile))
  # your ship details
  with open(saveFile, 'r') as file:
    saveFile = yaml.safe_load(file)
  return saveFile

def autoSave(fileName, saveFile):
  tmpSaveFileName = fileName + '.tmp'
  yamlOutput = yaml.dump(saveFile)
  print(yamlOutput)
  with open(tmpSaveFileName, 'w') as file:
    file.write(yamlOutput)

def loadingScreen(saveFile):
  clear()
  print('\n\n\nWelcome Traveller!')
  input("\n\n... Enter any key to continue ... ")
  if saveFile == False:
    loadGame = input('Do you want to load a saved game?\n> ')
    if loadGame in yesses:
      clear()
      print('Please select one of the following games:')
      selectedGame = False
      while selectedGame == False:
        saves = os.listdir(saveDir)
        count = 0
        for file in saves:
          print(str(count + 1),'-',file)
          count += 1
        selectedSaveFile = int(input('Which save file do you want to load?\n> '))
        print(selectedSaveFile)
        try:
          saveFile = saves[selectedSaveFile - 1]
          selectedGame = True
        except:
          print('not a valid file')
    saveFile = saveDir + saveFile
  saveFileName = saveFile
  return saveFile, saveFileName

def playerInput(currentSystem, sector, parsecs, ship, saveFile):
  print('\nPress a key',keys)
  playerKey = getch.getch()
  possibleKey = False
  if playerKey == chr(27): # quit
    possibleKey = True
    exitGame = input('\nAre you sure you want to quit?\n> ')
    if exitGame in yesses:
      quit()
  for key in keys:
    if playerKey == key:
      possibleKey = True
      if key == '1': # ship view
        clear()
        print(ship)
      if key == '2': # map
        clear()
        printMap(currentSystem, sector, parsecs,ship['jump'])
      if key == '3': # jump
        saveFile = jumpScreen(currentSystem, sector, ship, saveFile)

  if possibleKey == False:
    print('invalid key',str(playerKey))

  return saveFile

def systemDetails(system, sector):
  if sector:
    world = worldSearch(system, sector)
  else:
    world = worldSearch(system)
  currentSystem = worldDetailed(world)
  return currentSystem

def jumpScreen(currentSystem, sector, ship, saveFile):
  clear()
  jumpRange = ship['jump']
  reachableSystems = jumpSearch(currentSystem,jumpRange)
  reachableWorlds = []
  for rSystem in reachableSystems['Worlds']:
    if rSystem['Name'] != currentSystem['WorldName']:
      reachableWorlds.append(rSystem)
  print('# You are in: ',currentSystem['WorldName'])
  print('# You can jump to: ')
  nearbySystems = {}
  count = 0
  for system in reachableWorlds:
    letter = letters[count]
    sys = system['Name']
    uwp = system['UWP']
    nearbySystems.update({letters[count] : system['Name']})
    print(letter,'-',sys,':',uwp)
    count += 1
  selectedWorld = input('Select a world (letter) for more info\n> ')
  selected = False
  for system in nearbySystems:
    if selectedWorld == system:
      selected = True
      world = worldSearch(nearbySystems[system], sector)
      world = worldDetailed(world)
  if selected == False:
    print('not a valid selection')
  else:
    print('Sector:',world['SectorName'],'Sub Sector:',world['SubsectorName'])
    print('World:',world['WorldName'],'\tUWP:',world['WorldUwp'])
    print('Remarks:',world['WorldRemarks'])
    uwp = uwpTranslator(world['WorldUwp'])
    for feature in uwp:
      print(feature,'-',uwp[feature])

    jumpQuestion = '\nDo you want to jump to ' + world['WorldName'] + '?\n> '
    jump = input(jumpQuestion)
    if jump in yesses:
      saveFile.update({'location' : { 'system' : world['WorldName'], 'sector' : world['SectorName'] }})
      return saveFile
  


main(saveFile)
