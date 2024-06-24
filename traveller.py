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
keys = { '1' : 'ship details', '2' : 'map view' }

# arguments, only accept save files
try:
  saveFile = sys.argv[1]
except:
  saveFile = False 

clear = lambda: os.system('clear')

yesses = ['Yes','yes','Y','y','Ye','ye','ya','Ya','Yup','yup']
nos    = ['No','no','N','n','Nope','nope','Nah','nah']
ship = {}

def main(saveFile): 
  saveFile = loadingScreen(saveFile)
  saveFile = loadSave(saveFile)
  system = saveFile['location']['system']
  sector = saveFile['location']['sector']
  ship = saveFile['ship'] 
  currentSystem = systemDetails(system,sector) 
  currentSystemName = currentSystem['WorldName']
  gameActive = True
  while gameActive == True:
    playerInput(currentSystem, sector, parsecs, ship)

def loadSave(saveFile):
  print('...loading',str(saveFile))
  # your ship details
  with open(saveFile, 'r') as file:
    saveFile = yaml.safe_load(file)
  return saveFile

def loadingScreen(saveFile):
  clear()
  print('\n\n\n\n\tWelcome Traveller!')
  input("\n\n\t ... Enter any key to continue ... ")
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
  return saveFile

def playerInput(currentSystem, sector, parsecs, ship):
  print('\nPress a key',keys)
  playerKey = getch.getch()
  #print('key is', playerKey)
  possibleKey = False
  for key in keys:
    if playerKey == key:
      possibleKey = True
      if key == '1': # ship view
        clear()
        print(ship)
      if key == '2': # map
        clear()
        printMap(currentSystem, sector, parsecs)
  if possibleKey == False:
    print('invalid key',str(playerKey))

def systemDetails(system, sector):
  if sector:
    world = worldSearch(system, sector)
  else:
    world = worldSearch(system)
  currentSystem = worldDetailed(world)
  return currentSystem

main(saveFile)
