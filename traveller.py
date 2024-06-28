#!/usr/bin/python3

from spaceMap import *
from tables import *
from possibleWorlds import *
from trade import *

import os

import datetime
import locale
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
  while gameActive == True:
    system = saveFile['location']['system']
    sector = saveFile['location']['sector']
    ship = saveFile['ship'] 
    currentSystem = systemDetails(system,sector) 
    currentSystemName = currentSystem['WorldName']
    saveFile = playerInput(currentSystem, sector, parsecs, ship, saveFile, saveFileName)
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

def playerInput(currentSystem, sector, parsecs, ship, saveFile, saveFileName):
  print('\nPress a key',keys)
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
        printTradeCodes(currentSystem, sector, ship)

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
  
def printTradeCodes(currentSystem, sector, ship):
  jumpRange = ship['jump']
  reachableSystems = jumpSearch(currentSystem,jumpRange)
  reachableWorlds = []
  for rSystem in reachableSystems['Worlds']:
    if rSystem['Name'] != currentSystem['WorldName']:
      reachableWorlds.append(rSystem)
  uwp = uwpTranslator(currentSystem['WorldUwp'])
  population = currentSystem['WorldUwp'][4]
  codes = calcTradeCodes(currentSystem['WorldName'],currentSystem['SectorName'])
  header = '# You are in: ' + str(currentSystem['WorldName']) + ' # has trade codes: ' + str(codes)

  # create purchaseable goods dict
  goodsPurchase = {}
  count = 0
  for code in codes:
    for goods in tradeGoods:
      if code in tradeGoods[goods]['availability']:
        letter = letters[count]
        namedGood = tradeGoods[goods]['type']
        tonsAvail, perTonBuy = goodsAvailable(namedGood, population, codes)
        purchasePrice = int(tonsAvail * perTonBuy)
        goodsPurchase.update( { namedGood : { 'letter' : letter, 'tons' : tonsAvail, 'purchase' : purchasePrice } })
        count += 1

  # create sellable goods dict
  goodsToSell = {}
  count = 0
  cargo = ship['cargo']['stored']
  for good in cargo:
    letter = letters[count]
    tonsAvail = cargo[good]
    perTonSell = sellGoods(good, codes)
    sellPrice = int(tonsAvail * perTonSell)
    goodsToSell.update( { good : { 'letter' : letter, 'tons' : tonsAvail, 'sell' : sellPrice } })
    count += 1

  trading = True
  while trading:
    # print out
    clear()
    print(header)
    print('---[ Goods for Purchase (p) ]---')
    goodStrings = []
    for good in goodsPurchase:
      goodStrings.append(good)
    
    rows = 5
    columns = int(len(goodStrings) / rows)
    if len(goodStrings) % rows != 0:
      columns += 1
    for i in range(rows):
      pos = i
      rowString = ' '
      for j in range(columns):
        if len(goodStrings[pos]) > 22: 
          tab = '\t'
        elif len(goodStrings[pos]) < 15:
          tab = '\t\t\t'
        else:
          tab = '\t\t'
        rowString = rowString + goodStrings[pos] + tab
        try:
          goodStrings[pos + rows]
          pos = pos + rows
        except:
          break
      print(rowString)

    print('\n---[   Goods to Sell  (s)   ]---')
    for good in goodsToSell:
      print(good)
  
    maxCargo = ship['cargo']['max']
    usedCargo = 0
    for storedGood in ship['cargo']['stored']:
      tonnage = ship['cargo']['stored'][storedGood]
      usedCargo += tonnage 
    availCargo = maxCargo - usedCargo
    print('\nYou currently have',maxCargo,'max and',availCargo,'available')
  
    print('\nWould you like to: (P) purchase a good, (S) view offers on your goods, (Q) Return to main') 
    playerKey = getch.getch()
    if playerKey in [ 'p', 's', 'q']:
      if playerKey == 'p':
        clear()
        print(header)
        print('Goods Availble:')
        for good in goodsPurchase:
          letter = goodsPurchase[good]['letter'] 
          tonsAvail = goodsPurchase[good]['tons'] 
          purchasePrice = goodsPurchase[good]['purchase'] 
          if len(good) >= 26:
            tabs = ''
          elif len(good) >= 19 and len(good) < 26:
            tabs = '\t'
          elif len(good) >=11 and len(good) < 19:
            tabs = '\t\t'
          elif len(good) < 11:
            tabs = '\t\t\t'
          print(letter,'-',good,tabs,tonsAvail,'tons \t\t Cr',locale.format_string('%d',purchasePrice,True))
        print('Which good would you like to purchase?')
        selectedGood = getch.getch()
      if playerKey == 's':
        print('sale menu place holder')
      if playerKey == 'q':
        trading = False
  

main(saveFile)
