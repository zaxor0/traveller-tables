#!/usr/bin/python3

import json
import requests
import sys
import time

# mgt2e pg 257
starportQuality = {
 'A' : { 'Quality' : 'Excellent', 'Berthing Cost' : '1D x Cr1000', 'Fuel' : 'Refined', 
         'Facilities' : 'Shipyard (all), Repair, Highport 6+', 'Bases' : 'Military  8+, Naval 8+, Scout 10+' },
 'B' : { 'Quality' : 'Good', 'Berthing Cost' : '1D x Cr500' , 'Fuel' : 'Refined', 
         'Facilities' : 'Shipyard (spacecraft), Repair, Highport 8+', 'Bases' : 'Military 8+, Naval 8+, Scout 9+' },
 'C' : { 'Quality' : 'Routine', 'Berthing Cost' : '1D x Cr100', 'Fuel' : 'Unrefined',
         'Facilities' : 'Shipyard (small craft), Repair, Highport 10+', 'Bases' : 'Military 10+ Scout 9+' },
 'D' : { 'Quality' : 'Poor', 'Berthing Cost' : '1D x Cr 10',  'Fuel' : 'Unrefined', 
         'Facilities' : 'Limited Repair, Highport 12+', 'Bases' : 'Scout 8+, Corsair 12+' },
 'E' : { 'Quality' : 'Frontier', 'Berthing Cost' : '0', 'Fuel': 'Unrefined', 'Facilities' : 'None', 'Bases' : 'Corsair 10+' },
 'X' : { 'Quality' : 'No Starport', 'Berthing Cost' : '0', 'Fuel': 'Unrefined', 'Facilities' : 'None', 'Bases' : 'Corsair 10+' }
 }

def worldSearch(world):
  print('searching for', world)
  searchUrl = "https://travellermap.com/api/search?q=exact:" + world
  response = requests.get(searchUrl)
  data = json.loads(response.text)
  results = []
  for result in data['Results']['Items']:
    try:
      results.append(result['World'])
    except:
      print('...')
  if len(results) > 1:
    selected = False
    while selected == False:
      print('Which sector are you in?')
      position = 0
      for world in results:
        print(str(position + 1),'-',world['Sector'])
        position += 1
      selection = int(input('# ')) - 1
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
  sectorName = str(world['SectorName']) 
  sectorName = sectorName.replace(' ','%20')
  url = 'https://travellermap.com/api/jumpmap?sector=' + sectorName + '&hex=' + str(world['WorldHex']) + '&style=poster&options=33008&jump=6'
  return url
