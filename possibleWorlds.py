#!/usr/bin/python3

import json
import requests
import sys
import time

def worldSearch(world, sectorName=False):
  print('Loading data from travellermap.com')
  if sectorName:
    sectorName = sectorName.replace(' ','%20')
    query = str(world + "%20in:" + sectorName)
    searchUrl = 'https://travellermap.com/api/search?q="' + query
  else:
    searchUrl = 'https://travellermap.com/api/search?q=exact:' + world 
  response = requests.get(searchUrl)
  data = json.loads(response.text)
  results = []
  for result in data['Results']['Items']:
    try:
      results.append(result['World'])
    except:
      pass
  if len(results) > 1:
    selected = False
    while selected == False:
      position = 0
      print('Possible Sectors:')
      for world in results:
        print(' ',str(position + 1),'-',world['Sector'])
        position += 1
      selection = int(input('Which sector are you in? ')) - 1
      try:
        world = results[selection]
        selected = True
      except:
        print('not a valid number')
    return world
  else:
    return results[0]

def worldDetailed(world): 
  sectorX = world['SectorX'] 
  sectorY = world['SectorY'] 
  hexX = world['HexX'] 
  hexY = world['HexY'] 
  worldDetailedURL = 'https://travellermap.com/api/credits?sx=' + str(sectorX) + '&sy=' + str(sectorY) + '&hx=' + str(hexX) + '&hy=' + str(hexY)
  response = requests.get(worldDetailedURL)
  return json.loads(response.text)

def jumpSearch(world, jump):
  jumpRange = jump
  jumpUrl = 'https://travellermap.com/api/jumpworlds?sector=' + str(world['SectorName']) + '&hex=' + str(world['WorldHex']) + '&jump=' + str(jumpRange)
  response = requests.get(jumpUrl)
  return json.loads(response.text)

def nearbyPlanets(world, jump):
  nearbyWorlds = jumpSearch(world, jump)
  planetsArray = []
  for planet in nearbyWorlds['Worlds']:
    if planet['Name'] != world:
      planetsArray.append(planet['Name'])
  return planetsArray, nearbyWorlds

def worldPoster(world):
  try: # data format provided by the world detailed results (called credits in the api)
    sectorName = str(world['SectorName']) 
    worldHex = str(world['WorldHex']) 
  except:
    pass
  try:  # data format provided by the jump search results
    sectorName = str(world['Sector'])
    worldHex = str(world['Hex'])
  except:
    pass
  sectorName = sectorName.replace(' ','%20')
  url = 'https://travellermap.com/print/world?sector=' + sectorName + '&hex=' + worldHex + '&style=poster'
  return url

def jumpMap(world):
  try: # data format provided by the world detailed results (called credits in the api)
    sectorName = str(world['SectorName']) 
    worldHex = str(world['WorldHex']) 
  except:
    pass
  try:  # data format provided by the jump search results
    sectorName = str(world['Sector'])
    worldHex = str(world['Hex'])
  except:
    pass
  sectorName = sectorName.replace(' ','%20')
  url = 'https://travellermap.com/api/jumpmap?sector=' + sectorName + '&hex=' + str(world['WorldHex']) + '&style=poster&options=33008&jump=6'
  return url

def travellerMap(world):
  try: # data format provided by the world detailed results (called credits in the api)
    sectorName = str(world['SectorName']) 
    worldHex = str(world['WorldHex']) 
  except:
    pass
  try:  # data format provided by the jump search results
    sectorName = str(world['Sector'])
    worldHex = str(world['Hex'])
  except:
    pass
  sectorName = sectorName.replace(' ','%20')
  url = 'https://travellermap.com/go/' + sectorName + '/' + worldHex 
  return url
