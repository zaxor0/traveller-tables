#!/usr/bin/python3

from mechanics import *
from tables import *
from mgt2e import *
from possibleWorlds import *

import os

import datetime
import locale
import math
import sys
import time
import yaml

# variables
saveDir = 'saves/'
worldName = ""
parsecs = 5

# player input options
keys = { '1' : 'ship details', '2' : 'map view' , '3' : 'Jump' , '4' : 'Trade', 'ESC' : 'Quit'}

# arguments, only accept save files
try:
  saveFile = sys.argv[1]
except:
  saveFile = False 

clear = lambda: os.system('clear')

try:
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') #use locale.format for commafication
except locale.Error:
    locale.setlocale(locale.LC_ALL, '') #set to default locale (works on windows)

letters = list(map(chr, range(97, 123)))
yesses = ['Yes','yes','Y','y','Ye','ye','ya','Ya','Yup','yup']
nos    = ['No','no','N','n','Nope','nope','Nah','nah']
ship = {}

def main(saveFile): 
  saveFile, saveFileName = loadingScreen(saveFile)
  saveFile = loadSave(saveFile)
  gameActive = True
  # main loop 
  while gameActive == True:
    printMainView(saveFile)
    saveFile = playerInput(saveFile)
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
  with open(tmpSaveFileName, 'w') as file:
    file.write(yamlOutput)

def saveGame(fileName, saveFile):
  saveFileName = fileName
  yamlOutput = yaml.dump(saveFile)
  with open(saveFileName, 'w') as file:
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
          if file.endswith('.yml'):
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

def printMainView(saveFile):
  clear()
  sector = saveFile['location']['sector']
  system = saveFile['location']['system']
  ship = saveFile['ship']['type']
  cargoMax = str(saveFile['ship']['cargo']['max'])
  cargoUsed = 0
  for cargo in saveFile['ship']['cargo']['stored']:
    cargoUsed =  cargoUsed + saveFile['ship']['cargo']['stored'][cargo]['tons']
  cargoUsed = str(cargoUsed)
  print('[   key |   Action     ][   Game Status           ]')
  print('|                      ||                         |')
  print('|    1. Ship Details   || Sector:',sector,'|')
  print('|    2. Star Map       || System:',system,'|')
  print('|    3. System Jump    || Ship:',ship,'|')
  print('|    4. Trade          || Cargo:',cargoUsed,'/',cargoMax,'|')
  print('|                      ||                         |')
  print('|                      ||                         |')
  print('|                      ||                         |')
  print('|                      ||                         |')
  print('|                      ||                         |')
  print('[                      ||                         ]')
  print('   press a key (1,2,3,4)')
  
#def playerInput(currentSystem, sector, parsecs, ship, saveFile, saveFileName):
def playerInput(saveFile):
  system = saveFile['location']['system']
  sector = saveFile['location']['sector']
  ship = saveFile['ship'] 
  currentSystem = systemDetails(system,sector) 
  currentSystemName = currentSystem['WorldName']
  #print('\nPress a key',keys)
  playerKey = getch.getch()
  possibleKey = False
  if playerKey == chr(27): # quit
    possibleKey = True
    exitGame = input('\nAre you sure you want to quit?\n> ')
    if exitGame in yesses:
      saveOrNot = input('\nDo you want to save?\n> ')
      if saveOrNot in yesses:
        saveGame(saveFileName, saveFile)
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
      if key == '4': # trade 
        saveFile = tradeMenu(currentSystem, sector, ship, saveFile)

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
    print('Sector:',world['SectorName'],'\nSub Sector:',world['SubsectorName'])
    print('World:',world['WorldName'],'\tUWP:',world['WorldUwp'])
    print('Remarks:',world['WorldRemarks'])
    uwp = uwpTranslator(world['WorldUwp'])
    for feature in uwp:
      print(feature,'-',uwp[feature])

    jumpQuestion = '\nDo you want to jump to ' + world['WorldName'] + '?\n> '
    jump = input(jumpQuestion)
    if jump in yesses:
      saveFile['day'] += 7
      saveFile.update({'location' : { 'system' : world['WorldName'], 'sector' : world['SectorName'] }})
      return saveFile
  
main(saveFile)
