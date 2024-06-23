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
keys = { 'm' : 'map view' }

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
  ship = loadShip(saveFile)
  worldName = ship['location']
  currentSystem = systemDetails(worldName) 
  currentSystemName = currentSystem['WorldName']
  gameActive = True
  while gameActive == True:
    playerInput(currentSystem, parsecs)

def loadShip(shipFile):
  print('...loading',str(shipFile))
  # your ship details
  with open(shipFile, 'r') as file:
    ship = yaml.safe_load(file)
  return ship

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

def playerInput(currentSystem, parsecs):
  print('\nPress a key',keys)
  playerKey = getch.getch()
  print('key is', playerKey)
  if playerKey == chr(27):
    print('ESCAPE')
  for key in keys:
    if playerKey == key:
      if key == 'm':
        clear()
        printMap(currentSystem, parsecs)
    else:
      print('invalid key',str(playerKey))

def systemDetails(worldName):
  #if sectorName:
  #  world = worldSearch(worldName, sectorName)
  #else:
  world = worldSearch(worldName)
  currentSystem = worldDetailed(world)
  return currentSystem

main(saveFile)
